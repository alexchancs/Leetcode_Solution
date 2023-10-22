import unittest

from Solution import Solution

class TestTwoSum(unittest.TestCase):

    def test_example_1(self):
        solution = Solution()
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(solution.twoSum(nums, target), [0, 1])

    def test_example_2(self):
        solution = Solution()
        nums = [3, 2, 4]
        target = 6
        self.assertEqual(solution.twoSum(nums, target), [1, 2])

    def test_example_3(self):
        solution = Solution()
        nums = [3, 3]
        target = 6
        self.assertEqual(solution.twoSum(nums, target), [0, 1])

if __name__ == '__main__':
    unittest.main()
