class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        for i in range(len(nums)):
            if i >0 and nums[i]==nums[i-1]:
                continue
            target = -nums[i]
            left,right = i+1,len(nums)-1
            while left < right :
                two_sum = nums[left] + nums[right]

                if two_sum >target:
                    right-=1
                elif two_sum < target:
                    left +=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    right -= 1
                    left+=1
                    while left < right and nums[left]==nums[left-1]:
                        left +=1
        return res
