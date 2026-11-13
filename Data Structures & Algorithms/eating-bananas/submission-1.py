class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # sum of the hour for given k sum [piles // k + (1 if pile % l >0 else 0)] this take O(n)
        # when the k geting lager the sum of hour to eat getting small
        # return the smallest k that statified sum of hour h

        # the largestet k for is max_pipe it take len(piles) hour
        # find k in 1~max_pipe that sum of the hour that statified sum of hour h take O(logm) us Binary search

        max_pile = max(piles)

        left,right = 1 ,max_pile

        while left < right :
            mid = (left+right)//2

            hours = sum([pile // mid + (1 if pile % mid >0 else 0) for pile in piles])
            if hours <= h:
                right = mid
            else :
                left = mid +1
        return left

# Output: 2
# Input: piles = [1,4,3,2], h = 9
# max_pile = 4
# l=1,r=4
# while l1<r4 T | m =(1+4)//2=2,hours= (1+2+2+1)= 6 | hours <= h -> r=m=2
# while l1<r2 T | m = (1+2)//2=1 hours=(1+4+3+2)= 10 | hours > h -> l=m+1=2
# while l2<r2 F -> return left=2 
