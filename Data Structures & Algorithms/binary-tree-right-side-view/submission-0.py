# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS cause we ned level of rightest T O(n) M O(n)
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        que=deque([root])
        res=[]
        while que :
            level=[]
            for _ in range(len(que)):
                node = que.popleft()
                if node :
                    level.append(node.val)
                    que.extend([node.left,node.right])
            if level :
                res.append(level.pop())
                    
        return res

# output [1,3,5]
# Input: root = [1,2,3,null,4,null,5]
# que=[1],res=[]
# while que T | level=[]|
#   for 0 in 1 -> node=1,if node T|level=[1],que=[2,3]|
# ->if level T | res=[1]
# while que T | level=[]|
#   for 0 in 2 -> node=2,if node T|level=[2],que=[3,null,4]
#   for 1 in 2 -> node=3,if node T|level=[2,3],que=[null,4,null,5]
# ->if level T| res=[1,3]
# while que T | level=[]|
#   for 0 in 4 -> node=null,if node F
#   for 1 in 4 -> node=4,if node T|level=[4],que=[null,5,null,null]
#   for 2 in 4 -> node=null,if node F
#   for 3 in 4 -> node=5,if node T|level=[4,5],que=[null,null,null,null]
# ->if level T| res=[1,3,5]
# while que F->return res=[1,3,5]
