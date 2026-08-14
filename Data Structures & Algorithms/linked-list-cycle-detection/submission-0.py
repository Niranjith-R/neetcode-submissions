# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        ptr = head
        arr = []
        while ptr:
            if ptr.next in arr:
                return True
            else:
                arr.append(ptr.next)
                ptr = ptr.next
            
        return False
