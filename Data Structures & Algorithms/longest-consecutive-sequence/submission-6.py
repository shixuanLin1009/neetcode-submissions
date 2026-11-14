class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find the start of Consective which is the larget numer in seq if i-1 in set than return
        # for each element in list store seen in map check if seen  #O(n)
        # store longest seq that in the list
        seen = set() 
        logest_con = 0
        for val in nums :#O(n)
            if val not in seen:
                seen.add(val)
            start = val
            while start-1 in seen:
                start -= 1
            count_con=1
            while start + 1 in seen:
                start +=1 
                count_con+=1

            logest_con = max(logest_con,count_con)
            print(logest_con)
        return logest_con

# Output: 7            
# nums=[0,3,2,5,4,6,1,1]
# seen = {},lc=0
# for val0 -> val0 not in seen T->seen={0} ->start=val0 -> while 0-1 in seen F