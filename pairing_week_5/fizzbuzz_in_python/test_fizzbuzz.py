import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

	def test_simple_should_return_the_number(self):
		self.assertEqual(FizzBuzz(1), 1)
		self.assertEqual(FizzBuzz(17), 17)
		self.assertEqual(FizzBuzz(23), 23)

	def test_multiple_3_should_return_fizz(self):
		self.assertEqual(FizzBuzz(3), "fizz")
		self.assertEqual(FizzBuzz(9), "fizz")

if __name__ == '__main__':
	unittest.main()
