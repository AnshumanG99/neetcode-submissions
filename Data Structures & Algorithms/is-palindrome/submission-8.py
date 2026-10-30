class Solution:
    def isPalindrome(self, s: str) -> bool:

        head = 0
        tail = len(s) - 1

        while head < tail:

            while not s[head].isalnum() and head < tail:
                head += 1
            
            while not s[tail].isalnum() and head < tail:
                tail -= 1
            
            if not s[head].lower() == s[tail].lower():
                return False
        
            head += 1
            tail -= 1

        return True