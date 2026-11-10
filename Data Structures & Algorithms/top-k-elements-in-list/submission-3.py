import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        heap=[]
        for key,value in freq.items():
            heapq.heappush(heap,(-value,key))
        res=[]
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res