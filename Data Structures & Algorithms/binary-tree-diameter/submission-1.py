# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def traverseLRN(self, node: Optional[Node], current_depth):
        if not node:
            return current_depth - 1
        
        left_depth = self.traverseLRN(node.left, current_depth + 1)
        right_depth = self.traverseLRN(node.right, current_depth + 1)

        left_amount = left_depth - current_depth
        right_amount = right_depth - current_depth
        
        current_sum = left_amount + right_amount

        if current_sum > self.diameter:
            self.diameter = current_sum
        
        return max(left_depth, right_depth)

    def diameterOfBinaryTree(self, root: Optional[Node]) -> int:
        self.traverseLRN(root, 0)
        return self.diameter
        
        