from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import division

import os
import sys

#*******************************************************************************
#   Initialize the python environment by adding the necessary local paths to
#   Python's search path.

MY_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# ADD TO PATH: Local project files
sys.path.append(os.path.join(MY_DIRECTORY, 'src'))

# ADD TO PATH: Local site packages
sys.path.append(os.path.join(
    MY_DIRECTORY,
    'venv_py27', 'lib', 'python2.7', 'site-packages'))

#*******************************************************************************
#   Define the lambda function entry point that will be executed by events.

import hello_lambda

def handler(event, context):
    """ The lambda function entry point

    :param event:
        Dictionary containing parameters related to the function call
    :param context:
        Runtime execution and environmental information for this event
    """

    results = hello_lambda.run(event)

    print('\n'.join([ '{}'.format(r[0]) for r in results[:20] ]))
    return 'Jargon Count: {}'.format(len(results))
