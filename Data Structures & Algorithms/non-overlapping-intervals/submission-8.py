class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()# T O(nlogn)
        
        cnt = 0
        prev_end = intervals[0][1]

        for interval in intervals[1:]:# T O(n)
            if interval[0] >= prev_end:# non-overlap
                prev_end = interval[1]
            else:
                prev_end=min(interval[1],prev_end)
                cnt +=1
        return cnt

        # name check
        
# Output: 1
# Input: intervals = [[1,2],[2,4],[1,4]]

# intervals.sort(),intervals=[[1,2],[1,4],[2,4]]
# prev_end = 0,cnt = 0
# for interval[1,2] in intervals:
#   if interval[0]1 >= prev_end0 T
#       prev_end2 = interval[1]2
# for interval[1,4] in intervals
#   if interval[0]1 >= prev_end2 F
#   elif interval[1]4 > prev_end2 T
#       cnt +=1,cnt=1
# for interval[2,4] in intervals
#   if interval[0]2 >= prev_end2 T
#        prev_end4 = interval[1]4
# return 1