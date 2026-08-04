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
        
        pass1 = pass2 = head
        clonedict = {}

        while pass1:
            clonedict[pass1] = Node(pass1.val)
            pass1 = pass1.next
        
        while pass2:
            if pass2.next:
                clonedict[pass2].next = clonedict[pass2.next]
            else:
                clonedict[pass2].next = None
            if pass2.random:
                clonedict[pass2].random = clonedict[pass2.random]
            else:
                clonedict[pass2].random = None

            pass2 = pass2.next
        
        if head:
            return clonedict[head]
        
        return None