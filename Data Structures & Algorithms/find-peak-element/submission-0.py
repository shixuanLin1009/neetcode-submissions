class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        

        low,high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) //2
            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid
        return high

        # Name check:nums,high,low,mid

#用 [1, 3, 2] dry run
# while 0 < 2 T:
#   1 = (0 + 2) //2
#   if 3 < 2 F
#   high1 = 1
# while 0 < 1 T:
#   0 = (0 + 1) //2
#   if 1 < 3 T
#       1 = 0 + 1
# while 1 < 1 F
# return 1
