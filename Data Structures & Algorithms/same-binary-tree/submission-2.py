# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both nodes are None return True
        if not p and not q:
            return True

        # if one is None and the other is not we have a mismatch
        if not p or not q:
            return False
        
        # recursively check left and right children for p and q
        l_children = self.isSameTree(p.left, q.left)
        r_children = self.isSameTree(p.right, q.right)

        # if both children return true
        if l_children and r_children:
            # make sure the vals are the same and return true
            if p.val == q.val:
                return True
        
        # otherwise there is a difference and return false
        return False