# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for l in lists:
            c = l
            while c:
                nodes.append(c.val)
                c = c.next

        nodes.sort()

        res = ListNode(0)
        cur = res
        for node in nodes:
            cur.next = ListNode(node)
            cur = cur.next

        return res.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
from itertools import count


class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        minHeap = []
        counter = count()

        for node in lists:
            if node:
                heapq.heappush(minHeap, (node.val, next(counter), node))

        res = ListNode(0)
        tail = res

        while minHeap:
            _, _, node = heapq.heappop(minHeap)
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(minHeap, (node.next.val, next(counter), node.next))

        tail.next = None
        return res.next


if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    lists = [l1, l2, l3]
    res = s.mergeKLists(lists)
    while res:
        print(res.val)
        res = res.next
