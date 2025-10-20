# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = None

        while head:
            aux = head.next
            head.next = result
            result = head
            head = aux

        return result

# Creating head nodes
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()
result = solution.reverseList(head)

#Printing result
while result:
    print(result.val, end = " ")
    result = result.next