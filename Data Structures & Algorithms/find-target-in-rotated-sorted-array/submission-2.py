class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # required O(logn) 用 left 與 rigt mid targrt 之間的關係 來判斷如何修改指針

        # 1. 尋找最小值索引 (cut)
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                # 最小值一定在 mid 的右邊
                left = mid + 1
            else:
                # 最小值就是 mid 或在 mid 的左邊，不能 - 1
                right = mid
        
        cut = left  # 迴圈結束時 left == right，即為最小值索引

        left,right = 0,cut-1
        while left <= right :
            mid = (left + right) //2 #向下取整
            if nums[mid] < target:
                left = mid +1
            elif nums[mid] > target:
                right = mid -1
            else:
                return mid


        left,right =cut , len(nums)-1
        while left <= right :
            mid = (left + right) //2 #向下取整
            if nums[mid] < target:
                left = mid +1
            elif nums[mid] > target:
                right = mid -1
            else:
                return mid


        return -1


