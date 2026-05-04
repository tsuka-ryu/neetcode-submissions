# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = deque()

        if root:
            queue.append(root)
        
        level = 0
        while len(queue) > 0:
            arr = []
            for i in range(len(queue)):
                curr = queue.popleft()
                arr.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            ans.append(arr)
            level+=1
        
        return ans