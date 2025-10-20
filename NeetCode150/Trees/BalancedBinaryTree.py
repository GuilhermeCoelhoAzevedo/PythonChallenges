# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.maxDepth(root)
        return self.balanced

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        if abs(left - right) > 1:
            self.balanced = False

        return 1 + max(left, right)

# [1, 2, 3, null, null, 4]
# [1, 2, 3, null, null, 4, null, 5]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.left.left = TreeNode(5)
solution = Solution()
print(solution.isBalanced(root))
