# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(r1, r2):
            if not r1 and not r2:
                return True
            
            if not r1 or not r2 or r1.val != r2.val:
                return False
            
            return sameTree(r1.right, r2.right) and sameTree(r1.left, r2.left)
        
    
        def findSubroot(r1):
            if not r1:
                return False

            if sameTree(r1, subRoot):
                return True
            
            return findSubroot(r1.right) or findSubroot(r1.left)
        
        return findSubroot(root)