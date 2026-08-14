# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        
        ptr = head
        arr = []
        while ptr:
            arr.append(ptr.val)
            ptr = ptr.next
        Dummy = ListNode()
        new = Dummy
        for i in arr[::-1]:
            new.next = ListNode(i)
            new = new.next
        
        return Dummy.next
        
