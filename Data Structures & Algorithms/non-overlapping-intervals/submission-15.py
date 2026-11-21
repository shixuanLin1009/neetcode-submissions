class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()# 
        cnt = 0 
        prev = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prev :
                prev = end
            else:
                cnt +=1
                prev = min(end, prev)    

        return cnt

# name check: intervals, cnt, prev, start,end
# Output: 1
# Input: intervals = [[1,2],[2,4],[1,4]]
# intervals = [[1,2],[1,4],[2,4]]
# cnt = 0 ,prev = 0
# for 1, 2 in intervals:
#   if 1 >= 0 T
#       2 = 2
# for 1, 4 in intervals:
#   if 1 >= 2 F
#   elif 4 > 2:
#       cnt +=1, cnt = 1
#       2 = min(4, 2)
# for 2, 4 in intervals:
#   if 2 >= 2 T
# return 1