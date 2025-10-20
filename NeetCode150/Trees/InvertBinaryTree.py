# Definition for a binary tree node.
from typing import Optional


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


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        #Swap nodes
        root.left, root.right = root.right, root.left

        #Recursive call with following noes
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# [1,2,3,4,5,6,7]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
solution = Solution()
root = solution.invertTree(root)

root.printTree()