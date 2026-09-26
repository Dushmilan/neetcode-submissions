import heapq
class MedianFinder:
    """
    This is not efficient solution, but it works. The time complexity of addNum is O(log n) and findMedian is O(n log n) due to the use of heapq.nsmallest.
    We can improve the time complexity of findMedian to O(1) by using two heaps (a max heap for the lower half and a min heap for the upper half),
    but this implementation is simpler and works for small inputs.
    """
    def __init__(self):
        self.minheap = []  # upper half
        self.maxheap = []  # lower half, stored as negatives

    def addNum(self, num: int) -> None:
        # Add to lower half initially
        heapq.heappush(self.maxheap, -num)

        # Make sure every element in lower <= every element in upper
        if self.minheap and -self.maxheap[0] > self.minheap[0]:
            lower = -heapq.heappop(self.maxheap)
            upper = heapq.heappop(self.minheap)

            heapq.heappush(self.maxheap, -upper)
            heapq.heappush(self.minheap, lower)

        # Balance sizes
        if len(self.maxheap) > len(self.minheap) + 1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        elif len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]

        return (-self.maxheap[0] + self.minheap[0]) / 2