# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que=deque([root])
        res=[]
        while que:
            level=[]
            for _ in range(len(que)):
                node=que.popleft()
                if node:
                    que.extend([node.left,node.right])
                    level.append(node.val)
            if level:
                res.append(level)
        return res