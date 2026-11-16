class KthLargest:
# M : O(k)
    def __init__(self, k: int, nums: List[int]):
        self.minHeap,self.k=nums,k
        heapq.heapify(self.minHeap)#O(n)
        while len(self.minHeap) > k :#O(logn)
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        
        heapq.heappush(self.minHeap,val) #O(logk)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]