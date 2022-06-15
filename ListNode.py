# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        first = None
        second = head
        while second:
            next_tmp = second.next
            second.next = first
            first = second
            second = next_tmp
        
        return first
#o(n)
#o(1)
