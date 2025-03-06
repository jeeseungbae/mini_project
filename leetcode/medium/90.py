import unittest
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                result.append(subset[::])
                return

            # Subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return result


class TestSolution(unittest.TestCase):
    def test01(self):
        nums = [1,2,2]
        answer = [[],[1],[1,2],[1,2,2],[2],[2,2]]
        result = Solution().subsetsWithDup(nums)
        assert answer == result