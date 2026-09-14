class Solution:
    # anti-clock wise rotation
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            # Find the mid index
            mid = left + (right - left) // 2

            # If the mid element is greater than the rightmost element,
            # the minimum value must be in the right half of the array
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # If the mid element is less than or equal to the rightmost element,
                # the minimum value must be in the left half of the array (including mid)
                right = mid
        # When left == right, we have found the minimum element
        return nums[left]