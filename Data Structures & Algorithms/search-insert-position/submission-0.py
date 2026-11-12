class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # O(log n) is required using Binary search

        left,right = 0 , len(nums)-1

        while left <= right : 
            mid = (left + right) // 2 # 向下取整（偏左）
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return left 


        # mid + 1有可能跳過


#Output: 4
#Input: nums = [-1,0,2,4,6,8], target = 5
#left = 0 right = 5
# while left <=right T ->mid=0+5//2=2 nums[mid 2] = 2 < target -> left = mid + 1 = 3
# while T -> mid =3+5//2=4 nums[mid 4]=6 >target 5 -> r =m-1= 3
# while T -> mod = 3+3 //2 =3 nums[m 3]=4 <target -> left =m+1 = 4 # 就是要放的位置
# while F
# return left 4

#Output: 1
#Input: nums = [1], target = 2
#left = 0 right = 0
# while T -> mid = 0+0//2 nums[m 0]=1 <target 2 -> left =m +1 ->1 # 就是要放的位置
# return left 1

