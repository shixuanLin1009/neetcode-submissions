class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
     
        res = []
        combination=[]

        def dfs(i,target):
            
            if i >= len(nums):
                return None

            if target == 0:
                res.append(combination.copy())
                return
            if target < 0:
                return None
            #選
            combination.append(nums[i])
            dfs(i,target-nums[i])
            #不選
            combination.pop()
            dfs(i+1,target)

        dfs(0,target)

        return res

# Output: [[2,2,5],[9]]
# Input:nums = [2,5,6,9],target = 9
#   res = [],combination=[]
#   dfs(i0,target9)
#       if i > len(nums)4 F
#       if target == 0 F
#       if target < 0 F
#       combination.append(nums[i]),combination=[2]
#       dfs(i0,target9-nums[i0]2 7)
#           if i0 > len(nums)4 F
#           if target7 == 0 F
#           if target < 0 F
#           combination.append(nums[i]),combination=[2,2]
#           dfs(i0,target7-nums[i]2 5)
#               if i0 > len(nums)4 F
#               if target5 == 0 F
#               if target5 < 0 F
#               combination.append(nums[i]2),combination=[2,2,2]
#               dfs(i0,target5-nums[i]2 3)
#                   if i0 > len(nums)4 F
#                   if target3 == 0 F
#                   if target3 < 0 F
#                   combination.append(nums[i]2),combination=[2,2,2,2]
#                   dfs(i0,target3-nums[i]2 1)
#                       if i0 > len(nums)4 F
#                       if target1 == 0 F
#                       if target1 < 0 F
#                       combination.append(nums[i]2),combination=[2,2,2,2,2]
#                       dfs(i0,target1-nums[i]2 -1)->None
#                           if i0 > len(nums)4 F
#                           if target-1 == 0 F
#                           if target-1 < 0 T
#                               return None
#                       combination.pop(),combination=[2,2,2,2]
#                       dfs(i+1 1,target1)
#                           if i1 > len(nums)4 F
#                           if target1 == 0 F
#                           if target1 < 0 F
#                           combination.append(nums[i]5),combination=[2,2,2,2,5]
#                           dfs(i1,target1-nums[i]5 -4)->None
#                               if i1 > len(nums)4 F
#                               if target-4 == 0 F
#                               f target-4 < 0 T
#                                   return None
#                           combination.pop(),combination=[2,2,2,2]
#                           dfs(i+1,target)
