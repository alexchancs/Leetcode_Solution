import unittest

from Solution import Solution

class TestRoman(unittest.TestCase):
    def test_example(self):
        solution = Solution()
        s = "MCMXCIV"
        self.assertEqual(solution.romanToInt(s), 1994)

if __name__ == "__main__":
    unittest.main()



