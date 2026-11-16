class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= result[-1][1]:     # 跟最後一個重疊
                result[-1][1] = max(end,result[-1][1])        # 延長最後一個的終點
            else:
                result.append([start,end])               # 不重疊就新開一個
        return result