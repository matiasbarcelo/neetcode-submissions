# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverseLRN(self, node: Optional[TreeNode], current_level: int):
        if not node:
            return current_level - 1
        left_child_level_depth = self.traverseLRN(node.left, current_level + 1)
        right_child_level_depth = self.traverseLRN(node.right, current_level + 1)

        if left_child_level_depth >= right_child_level_depth:
            return left_child_level_depth
        else:
            return right_child_level_depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 1

        return self.traverseLRN(root, level)
        