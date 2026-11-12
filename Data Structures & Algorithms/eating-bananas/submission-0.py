class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left,right =1, max(piles)

        while left < right :# logn
            mid = (left+right) // 2

            hours = 0

            for pile in piles : #logn
                hours += pile // mid + (1 if pile % mid > 0 else 0)

            if hours <= h  :
                right = mid
                
            elif hours > h:
                left = mid + 1

        return left

