import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result= []
        for i in range(len(nums)):
            current_list = nums[:i] + nums[i+1:]
            result.append(math.prod(current_list))
        return result
            