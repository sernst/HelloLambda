from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import division

import os
import sys
import zipfile

PROJECT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

PACKAGES = ['github', 'six']

def doZip():
    filename = os.path.join(PROJECT_DIRECTORY, 'hello_lambda.zip')
    if os.path.exists(filename):
        os.remove(filename)

    zipper = zipfile.ZipFile(file=filename, mode='w')

    for root, dirs, files in os.walk(PROJECT_DIRECTORY):
        for filename in files:
            path = os.path.join(root, filename)
            if path == zipper.filename:
                continue

            if path.find('venv_py27') != -1:
                if path.find('tests') != -1:
                    continue

                found = False
                for p in PACKAGES:
                    if path.find('site-packages/{}'.format(p)) != -1:
                        found = True
                        break

                if not found:
                    continue

            zipper.write(
                filename=path,
                arcname=path[len(PROJECT_DIRECTORY):])

    zipper.close()

if __name__ == '__main__':
    import argparse
    import textwrap
    dedent = textwrap.dedent
    parser = argparse.ArgumentParser()

    parser.description = dedent("""
        deploy creates the lambda function distribution packages""")

    doZip()
    print('SUCCESS: Deployment zip created')
    sys.exit(0)

