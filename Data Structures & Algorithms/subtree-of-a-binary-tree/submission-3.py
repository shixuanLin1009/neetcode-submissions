# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def same(node,subRoot):
            if not node and not subRoot:
                return True
            if not node or not subRoot:
                return False
            if same(node.left,subRoot.left) and same(node.right,subRoot.right) and node.val ==subRoot.val:
                return True
            else:
                return False

        def dfs(node):
            if not node:
                return False
            return same(node,subRoot) or dfs(node.left) or dfs(node.right)

        return dfs(root)


