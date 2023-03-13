import unittest

from arrays.twoSum import TwoSum


class TestTwoSum(unittest.TestCase):

    def setUp(self):
        self.solution = TwoSum()

    def test_two_sum_case_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected_output = [0, 1]
        self.assertEqual(self.solution.two_sum(nums, target), expected_output)

    def test_two_sum_case_2(self):
        nums = [3, 2, 4]
        target = 6
        expected_output = [1, 2]
        self.assertEqual(self.solution.two_sum(nums, target), expected_output)

    def test_two_sum_case_3(self):
        nums = [3, 3]
        target = 6
        expected_output = [0, 1]
        self.assertEqual(self.solution.two_sum(nums, target), expected_output)


if __name__ == '__main__':
    unittest.main()
