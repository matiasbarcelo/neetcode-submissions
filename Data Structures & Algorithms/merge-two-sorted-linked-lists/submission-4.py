# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current_node = list1
        all_values = []
        all_nodes = []

        if current_node:
            all_values.append(current_node.val)
            all_nodes.append(current_node)
            current_node = current_node.next

        while current_node:
            l_index = 0
            r_index = len(all_values) - 1
            while l_index <= r_index:
                m = (l_index + r_index) // 2
                if current_node.val >= all_values[m]:
                    l_index = m + 1
                else:
                    r_index = m - 1
            if current_node.val >= all_values[m]:
                index = m + 1
                all_values.insert(index, current_node.val)
                all_nodes.insert(index, current_node)
            else:
                index = m
                all_values.insert(index, current_node.val)
                all_nodes.insert(index, current_node)
            current_node = current_node.next

        current_node = list2
        if not all_values and current_node:
            all_values.append(current_node.val)
            all_nodes.append(current_node)
            current_node = current_node.next
    
        while current_node:
            l_index = 0
            r_index = len(all_values) - 1
            while l_index <= r_index:
                m = (l_index + r_index) // 2
                if current_node.val >= all_values[m]:
                    l_index = m + 1
                else:
                    r_index = m - 1
            if current_node.val >= all_values[m]:
                index = m + 1
                all_values.insert(index, current_node.val)
                all_nodes.insert(index, current_node)
            else:
                index = m
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