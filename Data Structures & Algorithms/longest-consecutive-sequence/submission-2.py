from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(nums)
        longest = 1
        curr_result = 1

        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                curr_result+=1
                longest = max(longest,curr_result)
            elif nums[i] == nums[i-1]:
                continue
            else:
                curr_result = 1
        return longest