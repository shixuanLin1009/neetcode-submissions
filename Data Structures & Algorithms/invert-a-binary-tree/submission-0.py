# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# DFS stack
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        stack=[root]

        while stack:
            node = stack.pop()
            if node:
                temp = node.left
                node.left = node.right
                node.right = temp
                stack.extend([node.left,node.right])
        
        return root

# Output: [1,3,2,7,6,5,4]                
# Input: root = [1,2,3,4,5,6,7]
# root=1,stack=[1]
# while stack T | node=stack.pop()=1 ,if node T | temp=n.l=3,left=n.r=2,right=temp=3,stack=[2,3]
# while stack T | node=stack.pop()=3 ,if node T | temp=n.l=6,left=n.r=7,right=temp=6,stack=[2,6,7]
# while stcak T | node=stack.pop()=7 ,if node T | temp=n.l=None,left=n.r=None,right=temp=None,stack=[2,6,None,None]
# while stack T | node=stack.pop()=Nond if node F|
# while stack T | node=stack.pop()=Nond if node F|
# while stack F | node=stack.pop()=Nond if node F|
