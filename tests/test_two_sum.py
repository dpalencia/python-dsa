from pdsa import TwoSumSolution
import unittest
class TestTwoSum(unittest.TestCase):
    """
    Solution for 
    https://leetcode.com/problems/two-sum/submissions/
    """
    def test_two_sum(self):
        test_array = [2,7,11,15]
        two_sum_solution = TwoSumSolution()
        solution = two_sum_solution.twoSum(test_array, 9)
        assert(solution == [0, 1])

if __name__ == "__main__":
    unittest.main()