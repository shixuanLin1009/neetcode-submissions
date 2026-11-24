class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        visit = {}
        for i,num in enumerate(nums):# T O(n)
            if num in visit and abs(visit[num] - i) <= k:
                return True
            visit[num] = i
        return False
# Output: true
# Input: nums = [1,2,3,1], k = 3
# visit = {}
# for 0,1 is enumerate(nums):# T O(n)
#   if 1 in {} and abs(visit[num] - i) <= kF
#   visit[1] = 0
# for 1,2 is enumerate(nums):# T O(n)
#   if 2 in {} and abs(visit[num] - i) <= kF
#   visit[2] = 1
# for 2,3 is enumerate(nums):# T O(n)
#   if 1 in {} and abs(visit[num] - i) <= kF
#   visit[3] = 2
# for 3,1 is enumerate(nums):# T O(n)
#   if 1 in {} and abs(0 - 3) <= 3T
#       reutn True
