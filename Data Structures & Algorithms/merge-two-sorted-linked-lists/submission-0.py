# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 用two point 分別從兩個list頭開使比大小比較小的指針往後，依序比到最後
        dummy = ListNode() #dummy 變數 指向 ListNode(0,None)
        tail = dummy     # tail 永遠指向「新串列的最後一個」,且 tail 與 dummy 都指向 ListNode(0,None)
        while list1 and list2:   # 兩邊都還有才比
            if list1.val <= list2.val:
                tail.next = list1    # 接上較小的節點 把ListNode(0,None)改成ListNode(0,list1)
                list1 = list1.next  # 把 list 從 ListNode(val,next)改成ListNode(nxtVal,nxtNext)
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next # tail 往後走一步 把 tail變數改成 從 ListNode(0,list1)的next= ListNode(val,next)

        tail.next = list1 or list2   # 剩下那條整段接上
        return dummy.next

