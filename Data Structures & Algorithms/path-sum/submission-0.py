# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def leafSum(root, sum):
            if not root:
                return False
            sum = root.val + sum

            if not root.left and not root.right and sum == targetSum:
                return True
            if leafSum(root.left, sum):
                return True
            if leafSum(root.right, sum):
                return True
            return False

        return leafSum(root, 0)
