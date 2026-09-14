class Solution:
    def countBits(self, n: int) -> List[int]:
        return_array = []
        for i in range(n + 1):
            return_array.append(bin(i).count('1'))
        return return_array