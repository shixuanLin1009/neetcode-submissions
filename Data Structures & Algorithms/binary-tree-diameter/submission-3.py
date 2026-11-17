# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.longest = 0

        def dfs(node):
            if not node :
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.longest = max(self.longest,left+right)

            return 1+max(left,right)
        dfs(root)

        return self.longest
# Output: 3
# Input: root = [1,null,2,3,4,5]
# l=0
# dfs(root1)
#   if not node F
#   path=dfs(node.leftNone)+ dfs(node.right2)
#   dfs(node.leftNone)
#       if not node T:
#          return 0
#   dfs(node.right2)3
#       if not node F:
#       path=dfs(node.left3)2+dfs(node.right4)1
#       dfs(node.left3)2
#           if not node3 F:
#           path=dfs(node.left5)+dfs(node.rightnone)
#           dfs(node.left5)1
#               if not node 5:
#               path=dfs(node.leftnone)+dfs(node.rightnone)
#               dfs(node.leftnone)
#                   if not node T
#                       return 0 
#               dfs(node.rightnone)
#                   if not node T
#                       return 0 
#               self.longest0 = max(self.longest0,path0)
#               return 1+ max(dfs(node.left)0,dfs(node.right)0)
#           dfs(node.rightnone)0
#               if not node T
#                   return 0 
#           self.longest1 = max(self.longest0,path1)
#           return 1+ max(dfs(node.left)1,dfs(node.right)0)
#       dfs(node.right4)1
#           if not node4 F:
#           path=dfs(node.leftnone)+dfs(node.rightnone)
#           dfs(node.leftnone)
#               if not node T
#                   return 0 
#           dfs(node.rightnone)
#               if not node T
#                   return 0 
#            self.longest1 = max(self.longest1,path0)
#            return 1+ max(dfs(node.left)0,dfs(node.right)0)
#       self.longest3 = max(self.longest1,path3)
#       return 1+ max(dfs(node.left)2,dfs(node.right)1)
#   self.longest3 = max(self.longest3,path 3)
#   return 1+ max(dfs(node.left)0,dfs(node.right)3)
#