# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        res = ListNode(-1)
        res1 = ListNode(-1)
        res1.next = res
        carry =0
        
        while l1 or l2:
            if l1 and l2:
                sum_ = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                sum_ = l1.val + carry
                l1 = l1.next   
            else:
                sum_ = l2.val + carry
                l2 = l2.next
            value = sum_ % 10
            carry = sum_ // 10
            res.next = ListNode(value)
            res= res.next   
        if carry:
            res.next = ListNode(carry)
        return res1.next.next
        
            
         
        
            
                
                
        