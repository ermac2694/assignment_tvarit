import unittest
from find_sum import *


class TestSum(unittest.TestCase):

    def test_get_sum(self):
        self.assertEqual(get_sum(1, 2, 3), 6, "Should be 6")

    def test_is_integer_int(self):
        self.assertEqual(is_integer(1), True, "Integer Found")

    def test_is_integer_str(self):
        self.assertEqual(is_integer('1'), True, "Integer not Found")

    def test_sum_summation(self):
        self.assertEqual(calculate_sum([1, 2, 3]), (200, 6), "Should be 6")

    def test_sum_strc(self):
        self.assertEqual(calculate_sum([1, 2, 'a']), (400, "All inputs must be numeric"), "String found")
    
    def test_sum_strac(self):
        self.assertEqual(calculate_sum(['a', 2, 4]), (400, "All inputs must be numeric"), "String found")

if __name__ == '__main__':
    unittest.main()