# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy=ListNode()
        tail=dummy

        while list1 and list2 :
            if list1.val<=list2.val:
                tail.next=list1
                
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next
        tail.next=(list1 if list1 else list2 )

        return dummy.next

#Output: [1,1,2,3,4,5]
#Input: list1 = [1,2,4], list2 = [1,3,5]
# dummy->d(0)<-tail
# while list1 or list2 T->
#   list1.val1<=list2.v1 -> d(0)->l1(1)<-tail,list1=l1(2)
#   list1.v2>list2.v1 -> d(0)->l1(1)>l2(1)<-tail,list2=l2(3)
#   list1.v2<list2.v3 -> d(0)->l1(1)>l2(1)->l1(2)<-tail,list1=l1(4)
#   list1.v4>list2.v3 -> d(0)->l1(1)>l2(1)->l1(2)->l2(3)<-tail,list2=l2(5)
#   list1.v4<list2.v5 -> d(0)->l1(1)>l2(1)->l1(2)->l2(3)->l1(4)<-tail,list1=none
# while list1 none or list2 l2(5) F
# tail.next=(list1 if list else list2)=list2->-> d(0)->l1(1)>l2(1)->l1(2)->l2(3)->l1(4)->l2(5)<-tail,
# return dummy.next l1(1)

