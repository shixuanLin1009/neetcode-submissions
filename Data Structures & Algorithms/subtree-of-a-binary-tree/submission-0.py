# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def compare_node(node1,node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if compare_node(node1.left,node2.left) and compare_node(node1.right,node2.right) and  node1.val == node2.val:
                return True
            else:
                return False

        def dfs(node):
            if not node :
                return False
            if find_root(node,subRoot):
                return True
            return dfs(node.left) or dfs(node.right)
            
        def find_root(node,sub_root):
            return compare_node(node,sub_root)
                
        return dfs(root)
        
               

