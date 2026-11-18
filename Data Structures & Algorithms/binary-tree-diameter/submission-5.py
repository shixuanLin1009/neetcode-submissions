# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest=0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest,left+right)

            return 1 + max(left , right)
        
        dfs(root)

        return self.longest
# Output: 2
# Input: root = [1,2,3]
# self.longest=0
# dfs(rootA(2))
#   if not nodeA(2) F
#   left1=dfs(nodeA(2).leftB(1))1
#       if not nodeB(1)F
#       left0 = dfs(nodeB(1).leftNone)0
#           if not nodeNone T
#               return 0
#       right0 = dfs(nodeB(1).rightNone)0
#           if not nodeNone T
#               return 0
#       self.longest0 = max(self.longest0,left0+right0)
#       return 1 + max(left0 , right0)
#   right1 = dfs(nodeA(2).rightC(3))1
#       if not nodeC(3) F
#       left0 = dfs(nodeC(3).leftNone)0
#            if not nodeNone T
#               return 0
#       right0 = dfs(nodeC(3).rightNone)0
#            if not nodeNone T
#               return 0
#       self.longest0 = max(self.longest0,left0+right0)
#       return 1 + max(left0 , right0)
#   self.longest2 = max(self.longest0,left1+right1)
#   return 1 + max(left1 , right1)
# return self.longest2

