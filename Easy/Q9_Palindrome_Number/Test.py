import unittest

from Solution import Solution

class TestPalindrome(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        x = 121
        self.assertTrue(solution.isPalindrome(x))
    
if __name__ == '__main__':
    unittest.main()






