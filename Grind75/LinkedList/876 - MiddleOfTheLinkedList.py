#https://leetcode.com/problems/middle-of-the-linked-list/description

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        aux = head
        count = 0
        while aux:
            count +=1
            aux = aux.next

        #Index of second middle node
        count = (count//2) + 1

        count2 = 0
        while head:
            count2+=1
            if count == count2:
                return head

            head = head.next

# Creating head nodes
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

solution = Solution()

result = solution.middleNode(head)

#Printing result
while result:
    print(result.val, end = " ")
    result = result.next

#Optimized solution:
"""
def middleNode(self, head):
    slow=head
    fast=head
    while(fast!=None and fast.next!=None):
        slow=slow.next
        fast=fast.next.next
    return slow
"""