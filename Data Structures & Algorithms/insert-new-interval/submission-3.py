class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        res=[]
        start,end = newInterval[0],newInterval[1]
        for i,interval in enumerate(intervals):
            if interval[1] < start: # non-overlap and earlier than new
                res.append(interval)
            elif interval [0] <= end : # overlap
                start = min(start,interval[0])
                end = max(end,interval[1])
            else:
                res.append([start, end])     # 先放合併好的
                return res + intervals[i:]
        res.append([start, end]) 
        return res