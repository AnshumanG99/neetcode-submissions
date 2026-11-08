"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        dictpass = head
        indexes = {}

        while dictpass:
            indexes[dictpass] = Node(dictpass.val)
            dictpass = dictpass.next
        
        pass2 = head

        while pass2:
            if pass2.next:
                indexes[pass2].next = indexes[pass2.next]
            if pass2.random:
                indexes[pass2].random = indexes[pass2.random]

            pass2 = pass2.next
    
        if head: 
            return indexes[head]
        
        return None
