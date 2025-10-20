# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # result = final result
        # aux = aux variable that walk through the nodes, with result memory location
        result = aux = ListNode()

        while list1 and list2:
            if list1.val > list2.val:
                aux.next = list2
                list2 = list2.next
            else:
                aux.next = list1
                list1 = list1.next

            #Walks to the next result node
            aux = aux.next

        #Whatever list stll has elements is added to the next node of results linkedlist
        aux.next = list1 or list2

        return result.next

#Creating nodes linkedlist1
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

#Creating nodes linkedlist2
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

solution = Solution()

result = solution.mergeTwoLists(list1, list2)

#Printing result
while result:
    print(result.val, end = " ")
    result = result.next