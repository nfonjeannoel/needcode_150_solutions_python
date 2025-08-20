# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next

class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


if __name__ == "__main__":
    # Create first sorted linked list: 1 -> 2 -> 4
    list1 = ListNode(1, ListNode(2, ListNode(4)))

    # Create second sorted linked list: 1 -> 3 -> 4
    list2 = ListNode(1, ListNode(3, ListNode(4)))

    # Merge the two lists
    merged_list = Solution().mergeTwoLists(list1, list2)

    # Print the merged linked list
    while merged_list:
        print(merged_list.val, end=" -> " if merged_list.next else "")
        merged_list = merged_list.next
    # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4