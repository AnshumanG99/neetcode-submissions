# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, oroot: Optional[TreeNode], osubRoot: Optional[TreeNode]) -> bool:
        
        
        def isSameTree(root, subroot):
            if not root and not subroot:
                return True
            
            if not root or not subroot or not root.val == subroot.val:
                return False
            
            return isSameTree(root.right, subroot.right) and isSameTree(root.left, subroot.left)

        def dfs(root):
            if not root:
                return False
            if isSameTree(root, osubRoot):
                return True
            return dfs(root.left) or dfs(root.right) 

        return dfs(oroot)
            