class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        dup = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                dup.add(nums[i])
        return len(dup)>=1