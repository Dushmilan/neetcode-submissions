class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_all(piles, k, h):
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / k)
            return total_hours <= h
        k =1
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if can_eat_all(piles, mid, h):
                right = mid
            else:
                left = mid + 1
        return left