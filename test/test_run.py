# run_spec.py [UNIT TEST]
# (C) 2015
# Scott Ernst

from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import division

import unittest

import hello_lambda

class run_spec(unittest.TestCase):

    def test_run(self):
        """ doc... """
        result = hello_lambda.run({'repo':'ansible/ansible'})
        print(result)
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(run_spec)
    unittest.TextTestRunner(verbosity=2).run(suite)



