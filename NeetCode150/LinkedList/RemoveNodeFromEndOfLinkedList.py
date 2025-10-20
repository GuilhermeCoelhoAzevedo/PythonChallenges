# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        aux = head
        count = 0
        while aux:
            count +=1
            aux = aux.next

        index = count - n

        if index == 0:
            return head.next

        aux = head
        count = 0
        while aux:
            if count == index:
                aux2.next = aux.next
                return head

            #Hold previous value
            aux2 = aux
            aux = aux.next
            count +=1

# Creating nodes of head
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

n = 2
solution = Solution()
result = solution.removeNthFromEnd(head, n)

#Printing result
while result:
    print(result.val, end = " ")
    result = result.next

#Optimal solution
"""
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next
"""