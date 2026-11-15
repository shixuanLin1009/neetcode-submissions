# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.ans=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        depth=self.depth(root)
        return self.ans

        
    def depth(self, root: Optional[TreeNode]) -> int:

        
        if not root:
            return 0
            
        self.ans=max(self.ans,self.depth(root.left)+self.depth(root.right))
        
        return 1 + max(self.depth(root.left),self.depth(root.right))

            
        
