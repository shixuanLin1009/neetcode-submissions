# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. 兩者都不存在（代表這條路徑走到底了，結構相同） -> True
        if not p and not q:
            return True
        
        # 2. 其中一個不存在（結構不同），或兩者都存在但值不相等 -> False
        if not p or not q or p.val != q.val:
            return False

        # 3. 走到這裡，代表「p 和 q 都存在，且 p.val == q.val」
        # 這時才繼續往下比對左右子樹
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        
        