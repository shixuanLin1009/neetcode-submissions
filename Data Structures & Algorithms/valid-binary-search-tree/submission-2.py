# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.vaild(root)

    def vaild(self,node: Optional[TreeNode],low=float('-inf'),high=float('inf'))-> bool:

        if not node:
            return True
        
        if node.val <= low or node.val >= high:
            return False

        return self.vaild(node.left,low,node.val) and self.vaild(node.right,node.val,high)

# Output: true 
# Input: root = [2,1,3]
# node=2,low=-inf,high=inf ,if not node F | if  2 < -inf F or 2 > inf F 
#   node=1,low=-inf,high=2 , if not node F | if 1<-inf F or 1 > 2 F->
#       node=None,low=-inf,hign=1,if not node T->return True
#       node=None,low=1,hign=2,if not node T->return True
#   node=3,low=2,high=inf , if not node F | if 3<2 F or 3 > inf F->
#       node=None,low=-inf,hign=1,if not node T->return True
#       node=None,low=1,hign=2,if not node T->return True
# return True and True

