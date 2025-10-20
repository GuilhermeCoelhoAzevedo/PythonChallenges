#https://leetcode.com/problems/invert-binary-tree/description/

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        #Swap nodes
        root.left, root.right = root.right, root.left

        #Recursive call with following noes
        self.invertTree(root.left)
        self.invertTree(root.right)

        #Return the root
        return root

# [4,2,7,1,3,6,9]
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
solution = Solution()
root = solution.invertTree(root)

root.printTree()