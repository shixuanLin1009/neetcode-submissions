class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        nums_set=set(nums)#O(n)
        for num in nums_set: # O(n)
            if num-1 not in nums_set:
                cur_num=num
                cur_count=1
                while cur_num+1 in nums_set:
                    cur_num+=1 
                    cur_count+=1
                longest=max(longest,cur_count)
        # total : O(n)
        return longest
