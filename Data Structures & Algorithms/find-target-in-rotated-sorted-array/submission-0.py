class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            # if the rightmost element is greater than the target, then the target is in the left half, else it is in the right half
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:  # left half is sorted
                if nums[left] <= target < nums[mid]:  # target is in the left half
                    right = mid - 1
                else:  # target is in the right half
                    left = mid + 1
            else:  # right half is sorted
                if nums[mid] < target <= nums[right]:  # target is in the right half
                    left = mid + 1
                else:  # target is in the left half
                    right = mid - 1 
        return -1