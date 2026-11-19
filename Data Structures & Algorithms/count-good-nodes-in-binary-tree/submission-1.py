# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #dfs with acertor information
        # visit don't visit again so T O(n)

        cnt_good = 0

        def dfs(node,max_value):
            nonlocal cnt_good 
            cur_max=max_value
            if not node :
                return None
            
            if node.val >= cur_max:
                cur_max= node.val
                cnt_good +=1

            dfs(node.left,cur_max)
            dfs(node.right,cur_max)

            return None

        dfs(root,root.val)

        return cnt_good

    #Name check


# Output: 4
# Input: root = [1,2,-1,3,4]
# good=[]
# dfs(rootA(1),root.val1)
#   cur_max1=max_value1
#   if not nodeA(1) F
#   if node.val >= max_value T
#       cur_max1= node.val1
#       good.append(node),good=[A(1)]
#   dfs(nodeA(1).leftB(2),cur_max1)
#       if not nodeB(2)F
#       if node.val2 >= max_value1:
#           cur_max2= node.val2
#           good.append(nodeB(2)),good=[A(1),B(2)]
#       dfs(node.leftB(2),cur_max2)
#           if node.val >= cur_max:

        