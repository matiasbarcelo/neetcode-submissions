# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # edge cases
        if not list1 and not list2:
            return None
        elif list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2

        if list1.val <= list2.val:
            head = list1
            node2 = list2
        else:
            head = list2
            node2 = list1
        
        node1 = head
        node3 = head.next

        while node2 != None or node3 != None:
            if not node3:
                node1.next = node2
                node1 = node2
                node2 = node2.next
                continue
            elif not node2:
                node1.next = node3
                node1 = node3
                node3 = node3.next
                continue

            # node 3 stays the same
            if node3.val >= node2.val:
                node1.next = node2
                node1 = node2
                node2 = node2.next
            # node 2 stays the same
            else:
                node1.next = node3
                node1 = node3
                node3 = node3.next

        return head