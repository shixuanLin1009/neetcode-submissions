# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.k=k
        self.res=0
        self.cnt=0
        self.inorder(root)
        return self.res

    def inorder(self,node):
        if not node: 
            return
        self.inorder(node.left)          # 1. 先走左邊（比較小的）
        self.cnt += 1          # 2. 拜訪自己：數到第幾個
        if self.cnt == self.k:   # 3. 數到第 k 個就記下來
            self.res = node.val
            return
        self.inorder(node.right)          # 4. 再走右邊
            
# [3,1,4,null,2]、k=1 
# node = 3 | if not node F | inorder(1)
#   node=1 | if not node F | inorder(none)
#       node=None |if not node T->return
#   self.cnt=1|self.cnt==self.k T -> res=node,val=1 return
# self.cnt+=1,inorder(4)
#   node = 4 | if not node F |inorder(none)
#       node = None |if not node T ->return
#   self.cnt=3,inorder(None)
#       node = None |if not node T ->return

