class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Build the frequency map (Your current logic)
        number_count = {}
        for num in nums:
            number_count[num] = number_count.get(num, 0) + 1
        
        # 2. Sort the dictionary keys by their values (counts)
        # We sort the keys, but use the value as the "key" for sorting
        sorted_numbers = sorted(number_count.keys(), key=lambda x: number_count[x], reverse=True)
        
        # 3. Return the first k elements
        return sorted_numbers[:k]