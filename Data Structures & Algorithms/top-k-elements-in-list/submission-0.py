from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        heap=[]
        for key,value in freq.items():
            heapq.heappush(heap,(-value,key)) #heapq 是min-heap 存負數變max-heap
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])#heapq.heappop(heap)[1] 彈出並取出 key（數字本身）
        return res