class Solution:
    def rob(self, nums: List[int]) -> int:
        
        mem={}
        #搶不搶 for each 
        def f(i):
            if i<0:
                return 0
            if i==0:
                return nums[i]
            if i in mem:return mem[i]

            mem[i]=max(nums[i]+f(i-2),f(i-1))

            return mem[i]

        return f(len(nums)-1)
# 2
# nums=[1,2]
# mem={}
# nums.reverse()[2,1]
# return f(len(nums)2-11)
#   f(1)
#       if i<0 F
#       if i<=1 T
#           return nums[i]

