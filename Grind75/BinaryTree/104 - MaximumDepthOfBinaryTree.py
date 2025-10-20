#https://leetcode.com/problems/maximum-depth-of-binary-tree/description

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        #Gets maximum depth between left and right nodes and adds 1 representing current node
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

#[3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(None)
root.left.right = TreeNode(None)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.maxDepth(root))