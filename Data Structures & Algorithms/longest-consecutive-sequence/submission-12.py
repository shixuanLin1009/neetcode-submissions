class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums) # T O(n)
        longest_con = 0

        for n in nums: # T O(n)
            if n - 1 in seen: #避免重複，只算開頭的
                continue
            cur = n
            cur_con = 0

            while cur in seen :
                cur +=1
                cur_con +=1
            longest_con = max(longest_con,cur_con)
        return longest_con

# Output: 4
# Input: nums = [2,20,4,10,3,4,5]
# seen={2,20,4,10,3,5},lc=0
# for n2 in seen ->
#   if 2-1 in seen F|cur=2,cc=0 ->
#       while cur2 in seen T -> cur=3,cc=1
#       while cur3 in seen T -> cur=4 cc=2
#       while cur4 in seen T -> cur=5 cc=3
#       while cur5 in seen T -> cur=6 cc=4
#       while cur6 in seen F
#   lc=max(lc0,cc4)=4
# for n20 in seen ->
#   if 20-1 in seen F|cur=20,cc=0 ->
#       while cur20 in seen T -> cur=21,cc=1
#       while cutr21 in seen F
#   lc=max(lc4,cc,1)=4
# for n4 in seen ->
#   if 4-1 in seen T -> continue
# for n10 in seen ->
#   if 10-1 in seen F|cur=10,cc=0 ->
#       while cur10 in seen T -> cur=21,cc=1
#       while cutr11 in seen F
#   lc=max(lc4,cc,1)=4
# for n3 in seen ->
#   if 3-1 in seen T -> continue
# for n4 in seen ->
#   if 4-1 in seen T -> continue
#return lc = 4