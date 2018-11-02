import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

    def test_simple_should_return_the_number(self):
		      self.assertEqual(FizzBuzz(1), 1)


if __name__ == '__main__':
	unittest.main()
