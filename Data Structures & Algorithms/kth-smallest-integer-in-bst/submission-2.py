# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.res = 0
        def inorder(node):
            if self.cnt >= k :
                return
            if not node :
                return 
            inorder(node.left)
            self.cnt += 1 #中序走訪 先走左 再走自己（中），最後是右邊
            if self.cnt == k : #如果樹很大，可以加上 if cnt >= k: return 真正的提早終止（Early Exit）
                self.res = node.val
                return 
            inorder(node.right)

        inorder(root)

        return self.res
# Output: 5
# Input: root = [4,3,5,2,null], k = 4
# cnt=0,res=0
# inorder(root4)
#   if not node4 F
#   inorder(node4.left3)
#        if not node3 F
#        inorder(node3.left2)
#           if not node2 F
#           inoder(node2.leftnone)
#               if not nodenonoe T
#           cnt=1
#           if cnt>=k F
#           inorder(node2.rightnone)
#               if not nodenone T
#       cnt=2
#       if cnt>=k F
#       inorder(node3.rightnone)
#               if not nodenone T
#       cnt=3
#       if cnt3>=k F
#    inorder(node4.right5)
#       if not node 5 F
#        inorder(node5.leftnone)
#           if not node none T
#       cnt=4
#       if cnt4>=k,res=node.val5
# return self.res =5