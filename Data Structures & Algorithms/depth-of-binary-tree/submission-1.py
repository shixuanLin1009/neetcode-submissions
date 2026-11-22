# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# dfs
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(node):
            if not node:
                return 0
            
            return 1 + (max(dfs(node.left), dfs(node.right)))

        return dfs(root)

        # name check:root,dfs,node
# Output: 3
# Input: root = [1,2,3,null,null,4]

# dfs(1):->3
#   if not node F
#   return 1 + (max(dfs(node.left)1, dfs(node.right)2))
#   dfs(2)->1
#       if not node F
#       return 1 + (max(dfs(node.left), dfs(node.right)))
#       dfs(none)->0
#           if not node T
#           return 0
#       dfs(none)->0
#   dfs(3)->2
#       if not node F
#       return 1 + (max(dfs(node.left), dfs(node.right)))
#       dfs(4)->1
#           if not node F
#           return 1 + (max(dfs(none), dfs(none)))
#       dfs(none)->0
# return 3