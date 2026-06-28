from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        main_pointer = 0
        while main_pointer < len(numbers):
            tracker = main_pointer + 1
            while tracker < len(numbers):
                if numbers[main_pointer] + numbers[tracker] == target:
                    return [main_pointer+1, tracker+1]
                tracker += 1
            main_pointer += 1
        return []