#KINGSLEY OTTO
#MIDTERM


import sys
import unittest

from Rational import*

class TestSuitRational(unittest.TestCase):
    def testsimplify(self):
        self.assertEqual(Rational.simplify(12/14), (6/7))
        self.assertEqual(Rational.simplify(24/36), (2/3))
        self.assertEqual(Rational.simplify(12/12), (1/1))
        self.assertEqual(Rational.simplify(98/70), (7/5))
        



def main(argv):
    unittest.main()

if __name__ == '__main__':
  main(sys.argv)
