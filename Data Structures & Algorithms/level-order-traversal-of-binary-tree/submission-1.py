# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS use que
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = deque([root])
        res = []
        
        while que :# O(n)
            level = []
            for _ in range(len(que)): 
                node=que.popleft()
                if node:
                    que.extend([node.left,node.right])
                    level.append(node.val)
            if level:
                res.append(level)
        return res

# Output: [[1],[2,3],[4,5,6,7]]
# Input: root = [1,2,3,4,5,6,7]
# que=[1],res=[]
# while que[1] T,level=[] ->
#   for 0 in len(que)1 -> node=A(1),que=[]|if node.l T,que=[2]|if node.r T ,que=[2,3]|level=[1]
#   res=[[1]]
# while que[2,3] T,level[] ->
#   for 0 in len(que)2 -> node=B(2),que=[3] | if node.l T,que=[3,4]|if node.r T, que=[3,4,5]|level=[2]
#   for 1 in len(que)2 -> node=C(3),que=[4,5]|if node.l T,que=[4,5,6]|if node.r T,que=[4,5,6,7]|level=[2,3]
#   res=[[1],[2,3]]
# while que[4,5,6,7] T,level=[]->
#   for 0 in len(que)4 -> node=D(4),que=[5,6,7]|if node.l F|if node.r F|level=[4]
#   for 1 in len(que)4 -> node=E(5),que=[6,7]|if node.l F|if node.r F|level=[4,5]
#   for 2 in len(que)4 -> node=F(6),que=[7]|if node.l F|if node.r F|level=[4,5,6]
#   for 3 in len(que)4 -> node=G(7),que=[]|if node.l F|if node.r F|level=[4,5,6,7]
#   res=[[1],[2,3],[4,5,6,7]]
# while que[]F
# return res
