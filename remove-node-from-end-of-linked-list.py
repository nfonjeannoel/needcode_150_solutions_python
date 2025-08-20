# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        removeIndex = len(nodes) - n
        if removeIndex == 0:
            return head.next

        nodes[removeIndex - 1].next = nodes[removeIndex].next

        return head


class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        N = 0
        while cur:
            N += 1
            cur = cur.next

        removeIndex = N - n
        if removeIndex == 0:
            return head.next

        cur = head
        for i in range(N - 1):
            if i + 1 == removeIndex:
                cur.next = cur.next.next
                break
            cur = cur.next

        return head


class Solution3:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummy.next

if __name__ == "__main__":
    # Create a linked list 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    n = 2
    new_head = Solution().removeNthFromEnd(head, n)

    # Print the modified linked list
    cur = new_head
    while cur:
        print(cur.val, end=" -> " if cur.next else "")
        cur = cur.next
    # Output: 1 -> 2 -> 3 -> 5
