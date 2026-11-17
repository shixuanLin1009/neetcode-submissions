class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #use array 
        intervals.sort()#T O(nlog)
        res =[]
        for interval in intervals:
            if not res :
                res.append(interval)
                continue
            if interval[0] <= res[-1][1] and interval[1] >= res[-1][0]: # overlap
               res[-1][0] = min(res[-1][0],interval[0])
               res[-1][1] = max(res[-1][1],interval[1])
            else:
                res.append(interval)

        return res
# Output: [[1,5],[6,7]]
# Input: intervals = [[1,3],[1,5],[6,7]]
# res = []
# for interval[1,3] in intervals -> if not res T,res=[[1,3]]
# for interval[1,5] in intervals -> if not res F|if interval[0]1 <= res[-1][1]1 and interval[1]5 >= res[-1][0]3 T,res[-1][0]1 = min(res[-1][0]1,interval[0]1), res[-1][1]5 = max(res[-1][1]3,interval[1]5)
# for interval[6,7] in intervals ->  if not res F | if interval[0]6 <= res[-1][1]5 and interval[1]7 >= res[-1][0]1 F,res=[[1,5],[6,7]]
# return res=[[1,5],[6,7]]
              
