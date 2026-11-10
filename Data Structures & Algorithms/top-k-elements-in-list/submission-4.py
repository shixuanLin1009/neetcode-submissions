import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)  # ① 掃過 n 個數字   O(n)
        heap=[(-v,key) for key,v in freq.items()]
        heapq.heapify(heap)
        res=[]
        for _ in range(k):
            res.append(heapq.heappop(heap)[1]) # 每次 push O(log m)  → O(m log m)
        return res