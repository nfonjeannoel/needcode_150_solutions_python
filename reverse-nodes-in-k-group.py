# Definition for singly-linked list.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup = dummy

        while True:
            kth = self.getKth(prevGroup, k)
            if not kth:
                # unable to creat group if len k
                break
            nextGroup = kth.next

            # reverse till next Group]
            prev = kth.next  # so that current will point to prev
            cur = prevGroup.next  # start of current group

            while cur != nextGroup:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            # attach current proup to previous and update previous
            tmp = prevGroup.next
            prevGroup.next = kth
            prevGroup = tmp

        return dummy.next

    def getKth(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    k = 2
    result = s.reverseKGroup(head, k)
    while result:
        print(result.val)
        result = result.next