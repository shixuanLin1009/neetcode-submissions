# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#slow 一次走 1 步，fast 一次走 2 步。
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #兩個都從 head 出發，先走再比
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:#比較節點建議用 is，意思是「同一個物件」
                return True
        return False

# Output True
# Input A(1)->B(2)->C(3)->D(4)->B
# slow=A,fast=B
# while fastB and fast.nextC T| slowA==FastB F|slow=B,fast=B
# while fastB and fast.nextC T| slowB==FastB T -> return True

# Output False
# Input A(1)->B(2)
# slow=A,fast=B
# while fastB and fast.next None F| return False