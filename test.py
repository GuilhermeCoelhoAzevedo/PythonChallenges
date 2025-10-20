from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Print the tree
    def printTree(self):
        print(self.val, end=" ")
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()

# Definition for a binary tree node.
class Solution:
    def __init__(self):
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth(root)
        return self.max_diameter

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        self.max_diameter = max(self.max_diameter, left + right)

        return 1 + max(left, right)


# [1, 2, null]
#[1,2,2,3,3,3,null,null,null,null,null,4] - Expected False
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
#root.left.left = TreeNode(4)
#root.left.right = TreeNode(3)
#root.right.left = TreeNode(3)
#root.right.left.left = TreeNode(5)
#root.right.right = TreeNode(4)
#root.right.left.left = TreeNode(5)

solution = Solution()
print(solution.diameterOfBinaryTree(root))