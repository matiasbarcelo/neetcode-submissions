# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import bisect

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        all_values = []
        all_nodes = []

        current_node = list1
        while current_node:
            if not all_values:
                all_values.append(current_node.val)
                all_nodes.append(current_node)
                current_node = current_node.next
                continue
            index = bisect.bisect_right(all_values, current_node.val)
            all_values.insert(index, current_node.val)
            all_nodes.insert(index, current_node)
            current_node = current_node.next

        current_node = list2
        while current_node:
            index = bisect.bisect_right(all_values, current_node.val)
            all_values.insert(index, current_node.val)
            all_nodes.insert(index, current_node)
            current_node = current_node.next

        for i in range(len(all_nodes) - 1):
            all_nodes[i].next = all_nodes[i + 1]
            
        if all_nodes:
            all_nodes[-1].next = None
            return all_nodes[0]
        else:
            return None
