from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
from collections import Counter

import os
import re
import six
from github import Github
from hello_lambda.word_list import WORDS

MY_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIRECTORY = os.path.abspath(os.path.join(MY_DIRECTORY, '..', '..'))
DEFAULT_RANK = 5000
MAX_ISSUES = 100

def run(event):
    """ Function to handle the actual event execution.

    :param event:
        Parameters specified by the AWS Lambda function event
    """

    has_event_key(event, 'repo')

    configs = get_configs()
    g = Github(configs['GITHUB_TOKEN'])

    repo = g.get_repo(event['repo'])
    if not repo.has_issues:
        print('NO ISSUES: {}'.format(event['repo']))
        return []

    counter = Counter([])
    for issue in repo.get_issues().reversed[:MAX_ISSUES]:
        counter.update(to_words(issue.body))

    return sort_by_rank(counter)

def has_event_key(event, key):
    """ Checks that the event object has the specified key and raises an
        error if it does not
    """

    if key not in event or not event[key]:
        raise KeyError(
            'Invalid or missing "{}" in event:\n{}'.format(key, event))

def get_configs():
    """ Returns a dictionary instance of the configuration file values """

    with open(os.path.join(PROJECT_DIRECTORY, 'configs.json')) as f:
        return json.load(f)

def to_words(text):
    """ Breaks up the raw text into a word list """

    text = text \
        .strip() \
        .replace('\n', ' ') \
        .replace('  ', ' ') \
        .lower()

    text = re.sub(r'[^a-zA-Z]+', ' ', text)
    text = re.sub(r'\s{2,}', ' ', text)

    return text.split(' ')

def sort_by_rank(counter):
    """ Converts the counter keys and values to a list of tuples sorted by
        rank in descending order
    """

    results = []
    for key, value in six.iteritems(counter):
        if not len(key) > 2:
            continue

        rank = WORDS[key][0] if key in WORDS else DEFAULT_RANK
        results.append((key, value*rank*rank))

    # Sort the results by score and truncate the list at the minimum score
    # threshold.
    results.sort(key=lambda x: x[1], reverse=True)
    for r in results:
        if r[1] <= DEFAULT_RANK:
            results = results[:results.index(r)]
            break

    return results
