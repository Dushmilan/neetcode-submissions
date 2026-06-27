class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        dup = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.append(nums[i])
            else:
                dup.add(nums[i])
        return len(dup)>=1