class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    #我會先去做 sorted 把nums increasing order
    # 固定 i 把 -[nums] 當target 對後面的 數字做twosum=target來找
    # 後面會使用two pointer 若 左右指針相加大於target 因為右邊是最大值 往左移，two_sum會靠近 target 以此類推
    # time O(n^2)  space O(1)
    # 開始實作
        nums.sort()
        res = []

        for i,val in enumerate(nums):
            if i > 0 and val == nums[i-1]: 
                continue
            target = -val
            left = i+1
            right = len(nums)-1

            while left < right :
                #去重
                two_sum = nums[left] + nums[right]

                if two_sum > target:
                    right -= 1
                elif two_sum < target:
                    left += 1
                elif two_sum == target:
                    res.append([val,nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return res

