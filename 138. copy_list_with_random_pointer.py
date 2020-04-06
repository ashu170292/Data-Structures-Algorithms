"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dict_nodes = {}
        
        head_copy1 = head
        head_copy2 = head
        
        if not head:
            return None
        
        while head_copy1:
            dict_nodes[head_copy1] = Node(head_copy1.val)
            head_copy1 = head_copy1.next
        
        while head_copy2:
            if head_copy2.next in dict_nodes.keys():
                dict_nodes[head_copy2].next = dict_nodes[head_copy2.next]
            if head_copy2.random in dict_nodes.keys():
                dict_nodes[head_copy2].random = dict_nodes[head_copy2.random]
            head_copy2 = head_copy2.next
        
        return dict_nodes[head]
            
        
        

        
            
            
            
            
        
            
        
        