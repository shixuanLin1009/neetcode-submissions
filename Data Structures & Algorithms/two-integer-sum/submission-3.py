class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        visit = {}
        for i,num in enumerate(nums):
            need = target - num
            if need in visit: return [visit[need],i]
            else: visit[num] = i
        
        #name check : nums,target,,i,num,need,visit.
    

# Input: nums = [4,5,6], target = 10

# Output: [0,2]
# visit = {}
# for 0,4 in enumerate(nums):
#   6 = 10 - 4
#   if 6 in visit F
#       visit[4] = 0,visit={4:0,}
# for 1,5 in enumerate(nums):
#   5 = 10 - 5
#   if 5 in visit F
#       visit[5] = 1,visit={4:0,5:1}
# for 2,6 in enumerate(nums):
#   4 = 10 - 6
#   if 4 in visit T
#       return [0,2]
# Input: nums = [5,5], target = 10

# Output: [0,1]
# visit = {}
# for 0,5 in enumerate(nums):
#   5 = 10 - 5
#   if 5 in visit F
#       visit[5] = 0,visit={5:0,}
# for 1,5 in enumerate(nums):
#   5 = 10 - 5
#   if 5 in visit T
#       return [0,1]