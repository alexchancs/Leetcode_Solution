import unittest

from Solution import Solution

class CommonPrefixTest(unittest.TestCase):
    def test_example(self):
        solution = Solution()
        strs = ["flower","flow","flight"]
        self.assertEqual(solution.longestCommonPrefix(strs), "fl")

if __name__ == "__main__":
    unittest.main()