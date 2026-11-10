# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):

            if not node:
                return [True, 0]
            
            right = dfs(node.right)
            left = dfs(node.left)

            if not right[0] or not left[0]:
                return [False]

            diff = right[1] - left[1]

            if abs(diff) <= 1:
                return [True, 1 + max(right[1], left[1])]
            
            else:
                return [False]
        
        return dfs(root)[0]

        