# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        seen_nodes = []

        while node:
            if node in seen_nodes:
                return True
            seen_nodes.append(node)
            node = node.next

        return False