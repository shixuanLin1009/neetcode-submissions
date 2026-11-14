# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n):         # fast 先走 n 步
            fast = fast.next
        while fast.next:           # 一起走到 fast 是最後一個
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next # slow 的下一個就是要刪的
        return dummy.next