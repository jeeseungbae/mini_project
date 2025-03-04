from typing import List
import unittest


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k

class TestSolution(unittest.TestCase):
    def test01(self):
        nums = [1,1,1,2,2,3]
        answer = 5
        result = Solution().removeDuplicates(nums)
        print(result)
        assert answer == result