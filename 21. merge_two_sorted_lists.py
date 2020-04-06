# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        sorted_list = ListNode(None)
        
        previous = sorted_list
        
        while (l1 is not None) and (l2 is not None):
            
            if l1.val <= l2.val:
                #if sorted_list:
                previous.next = l1
                previous = previous.next

                l1= l1.next

#                 else:

#                     sorted_list = l1
#                     present_node = sorted_list
#                     l1 = l1.next
            else:
                #if sorted_list:
                previous.next = l2
                previous = previous.next

                l2 = l2.next

#                 else:

#                     sorted_list = l2
#                     l2 = l2.next
            #sorted_list = sorted_list.next
                    
                    
        if l1 is not None:
            
            previous.next = l1
            #return sorted_list
            
        else:
            
            previous.next = l2
        
        return sorted_list.next
        
        
            
            
                