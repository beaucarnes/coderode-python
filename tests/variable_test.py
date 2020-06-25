import unittest
import sys
sys.path.append('./src')

from blackjack import *

class VariableTest(unittest.TestCase):
    def test_add_no_numbers(self):
        self.assertEqual(rank, "K", "Variable named 'rank' should be set to 'K'")

if __name__ == '__main__':
    unittest.main()