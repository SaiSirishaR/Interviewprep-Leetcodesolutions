# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

## 2 conditions

# 1. if value of element in list 1< value of element in List 2, add the element in list 1 to the new linked list and increment the element in list 1 to next position

# edge case: Check if the lists are not of the same size and add the list with additional nodes to the final list

           dummy = ListNode()
           pointer = dummy

           while l1 and l2:
                 if l1.val < l2.val:
                     pointer.next = l1
                     l1 = l1.next
                 else:
                     pointer.next = l2
                     l2 = l2.next
                 pointer = pointer.next

           if l1:
              pointer.next = l1
           else:
               pointer.next = l2

           return dummy.next     



       
