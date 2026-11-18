class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res =[]
        start,end = newInterval[0],newInterval[1]
        n = len(intervals)
        i = 0
        while i < n:
            if intervals[i][1] < start: # non-overlap and earlier than new
                res.append(intervals[i])
                i += 1
            else:
                break
        while i < n:  
            if intervals[i][0] <= end : # overlap
                start = min(start,intervals[i][0])
                end = max(end,intervals[i][1])
                i += 1
            else:
                break
        res.append([start,end])

        while i < n:
            res.append(intervals[i]) # non-overlap and later than new
            i += 1        
        return res

# Output: [[1,6]]
# Input: intervals = [[1,3],[4,6]], newInterval = [2,5]
# res=[],start=2,end=5,n=2,i=0
# while i0<n2 T
#   if interval[i][1]3 < start2 F
#   break
# while i0 < n2 T
#   if interval[i0][0]3 <= end5 T
#       start1 = min(start2,interval[i0][0]1)
#       end5 = max(end5,interval[i0][1]3)
#       i += 1
# while i1 < n2 T
#   if interval[i1][0]4 <= end5 T
#       start1 = min(start1,interval[i1][0]4)
#       end6 = max(end5,interval[i][1]6)
#       i += 1
# while i2 <n2 F
# res.append([start1,end6]),res=[[1,6]]
#  while i2 < n2:
