# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            nxt = curr.next # 存下一個
            curr.next = prev # 上一個變下一個
            prev = curr # 上一個 變這個
            curr = nxt # 這個變下一個
        return prev 