# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cnt = 0
        if head is None:
            return head
        while head:
            pres = head
            sec = head.next
            if cnt == 0:
                pres.next = None
                cnt += 1
            else:
                pres.next= final    
            final = pres    
            head = sec
        return final
        
        
            
        
        
        
        
        
        
        