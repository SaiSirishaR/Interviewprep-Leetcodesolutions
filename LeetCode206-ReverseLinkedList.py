# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
          
###Linkedlist = group of nodes
###node = data, pointer (pointing towards the next node inside the linked list)

####array = [4,6,8,3], print(array[2])

### access the next node = [currentnode].next

          prev, cur = None, head

          while cur:
                temp_nxt = cur.next
                cur.next = prev
                prev = cur
                cur = temp_nxt
          return prev
