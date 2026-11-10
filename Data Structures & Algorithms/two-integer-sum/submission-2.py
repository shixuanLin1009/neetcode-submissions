class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index in range(len(nums)) :
            
            need = target-nums[index]
            if need in seen:
                return [seen[need],index]
            seen[nums[index]]=index