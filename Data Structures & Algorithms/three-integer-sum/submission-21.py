class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #先將nums sorted 後，對i 後面的做two_sum，遇到重複的要跳過
        res=[]

        nums.sort()
    
        for i,val in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target =- val
            left = i+1
            right = len(nums)-1
            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum > target :
                    right-=1
                elif two_sum <target :
                    left +=1
                else:
                    res.append([val,nums[left],nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left]==nums[left-1]:
                        left+=1
        return res

