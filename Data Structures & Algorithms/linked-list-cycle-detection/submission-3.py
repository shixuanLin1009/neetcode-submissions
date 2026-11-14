# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#slow 一次走 1 步，fast 一次走 2 步。
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            slow=head.next
            if slow:
                fast=slow.next
                while fast and fast.next:
                    if slow == fast :
                        return True
                    slow=slow.next
                    fast=fast.next.next
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