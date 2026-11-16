class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap,self.k=nums,k
        heapq.heapify(self.minHeap)#O(n)
        while len(self.minHeap) > k :#O(1)
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        
        heapq.heappush(self.minHeap,val) #O(logn)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]