#https://leetcode.com/problems/diameter-of-binary-tree/description

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
class Solution:
    def __init__(self):
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.maxDepth(root)

        return self.max_diameter

    def maxDepth(self, root: Optional[TreeNode]):
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        #Saves maximum diameter betweena all nodes
        self.max_diameter = max(self.max_diameter, left + right)

        #Gets maximum depth between left and right nodes and adds 1 representing current node
        return 1 + max(left, right)

#[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
#[1,2,3,4,5]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

solution = Solution()
print(solution.diameterOfBinaryTree(root))