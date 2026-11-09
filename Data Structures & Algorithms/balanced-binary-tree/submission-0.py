# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(tree):
            if not tree:
                return [True, 0]
            
            left, right = dfs(tree.left), dfs(tree.right)
           
            if not (left[0] and right[0]):
                return [False]
            

            difference = left[1] - right[1]

            if abs(difference) <= 1:
                return [True, max(left[1], right[1]) + 1]
            else:
                return [False]
        
        return dfs(root)[0]

        

        