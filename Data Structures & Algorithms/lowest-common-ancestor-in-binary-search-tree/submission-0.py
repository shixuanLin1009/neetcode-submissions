# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        return self.LCA(root,p,q)

    def LCA(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #如何找到p跟q
        #記住找過的level樹

        if p.val < root.val and q.val < root.val:
            # find p q in left
            LCA=self.LCA(root.left,p,q)
        if p.val > root.val and q.val > root.val:
            # find p q in right
            LCA=self.LCA(root.right,p,q)
        if min(p.val,q.val) <= root.val and max(p.val,q.val) >= root.val:
            # find p q in right
            LCA=root

        return LCA

# Output: 3
# Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4
# root=5| p3<q4<5 T |LCA=self.LCA(3,3,4)
#   root=3|p3<=3< q4 T | LCA=3
# LCA=3

