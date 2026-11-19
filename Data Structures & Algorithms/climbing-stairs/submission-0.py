class Solution:
    def climbStairs(self, n: int) -> int:
        # cache result memotization

        
        one,two = 1,1
        for i in range(n-1):
            tem=one
            one = one + two
            two = tem
            

        return one