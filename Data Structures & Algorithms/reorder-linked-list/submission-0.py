# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        arr = []
        ptr = head

        while ptr:
            arr.append(ptr)
            ptr = ptr.next

        a=0
        b = len(arr) - 1

        while a < b:
            arr[a].next = arr[b]
            a +=1
            if a == b:
                break
            arr[b].next = arr[a]
            b -= 1
        
        arr[a].next = None

            