class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i <= r:   # 如果 等於0 就跟左如果等於2就跟右邊換
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1

        # name check :nums,left,right,temp
# Input: nums = [1,0,1,2]
# Output: [0,1,1,2]
# left, right = 0,1
# while 1 < 4 T
#   if 1 > 0 T
#       temp 0 =  nums[right] 0
#       nums[right]1 = nums[left]1
#       nums[left]0 = temp0
#       nums =[0,1,1,2]
#   left += 1 ,left = 1
#   right += 1, right = 2
# while 2 < 4 T
#   if 1 > 1 F
#   left += 1 ,left = 2
#   right += 1, right = 3
# while 3 < 4 T
#   if 1 > 2 F
#   left += 1 ,left = 3
#   right += 1, right = 4
# while 4 < 4 F
