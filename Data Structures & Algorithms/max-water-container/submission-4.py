class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right=0,len(heights)-1
        res=0
        
        while left<right:
            area=(right-left)*min(heights[right],heights[left])
            res=max(res,area)
            if heights[right]<=heights[left]:
                right-=1
            elif  heights[right]>heights[left]:
                left+=1

        return res
