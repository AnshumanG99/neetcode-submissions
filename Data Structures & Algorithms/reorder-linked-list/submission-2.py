# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondhalf = slow.next
        slow.next = None
        reverse = None

        while secondhalf:
            temp = secondhalf.next
            secondhalf.next = reverse
            reverse = secondhalf
            secondhalf = temp
    


        answer = ListNode()
        while reverse:
            answer.next = head
            answer = answer.next
            head = head.next

            answer.next = reverse
            answer = answer.next
            reverse = reverse.next

        answer.next = head

        
