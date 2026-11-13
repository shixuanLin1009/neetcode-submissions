class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the cut point which is separate list into two increase  segent
        # find target in each increase-segment using binary search O(logn)
        # find the cut point which the first value that simotaounsly smaller than left and  right using  using binary search O(logn)

       
        #find Cut point
        cut=0
        left,right = 0,len(nums)-1
        while left < right:
            mid = (left + right)//2
            if nums[mid] <= nums[right]:
                right = mid
            else: 
                left = mid + 1
        cut = left 
        print(cut)
        #find target
        left,right = 0, cut-1
        while left <= right:
            mid = (left + right)//2
            
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                return mid

        left,right = cut, len(nums) - 1
       
        while left <= right:

            mid = (left + right)// 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                return mid

        return -1

