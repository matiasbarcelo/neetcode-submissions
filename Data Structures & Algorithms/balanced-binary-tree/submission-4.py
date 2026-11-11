# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recursiveLRN(self, node: Optional[TreeNode], current_level: int = 0, isRoot: bool = True):
        if not node:
            return current_level
        l_node = self.recursiveLRN(node.left, current_level + 1, False)
        r_node = self.recursiveLRN(node.right, current_level + 1, False)

        diff = abs(l_node - r_node)
        if diff > 1 or not l_node or not r_node:
            return False
        else:
            if isRoot:
                return True

            return max(l_node, r_node)
        

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.recursiveLRN(root)