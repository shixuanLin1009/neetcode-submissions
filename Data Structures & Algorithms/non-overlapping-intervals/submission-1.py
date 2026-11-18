class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        count = 0
        prev_end = intervals[0][1]
        for s, e in intervals[1:]:
            if s >= prev_end:          # 碰到不算重疊
                prev_end = e
            else:                      # 重疊：刪一個，留結束早的
                count += 1
                prev_end = min(prev_end, e)
        return count