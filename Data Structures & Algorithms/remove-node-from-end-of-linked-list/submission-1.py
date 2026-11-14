# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        tail = head
        length=0
        while tail :
            length+=1
            tail=tail.next
        target = length-n
        index = 0

        prev,curr=None,head
        while curr:
            nxt=curr.next
            if target == index:
                if prev:
                    prev.next=nxt
                    curr.next=None
                else:
                    head=head.next
            else:
                prev=curr
                curr =nxt
            index+=1
    
        return head


# A(1)->B(2)->C(3)->D(4) 
# prev = None curr=C,dummy=curr(3)
# 
# A(1)->B(2)->D(4)
# head=head.next

# A(1)->B(2)
# curr=H,
# dummy->B(2)
# head = A
# head = head.next B



