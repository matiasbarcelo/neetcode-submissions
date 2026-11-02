import copy
from typing import Optional
from collections import deque

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def traverseLRN(self, node : Optional[TreeNode]):
        if node == None:
            return
        self.traverseLRN(node.left)
        self.traverseLRN(node.right)
        # switch left and right to invert tree
        old_left = node.left
        node.left = node.right
        node.right = old_left

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if it's empty just return None
        if not root:
            return None
        self.traverseLRN(root)

        return root
