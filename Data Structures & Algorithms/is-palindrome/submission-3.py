class Solution:
    def isPalindrome(self, s: str) -> bool:
         
        left = 0
        right = len(s) - 1

        while left < right: 
            leftvalue = s[left]
            rightvalue = s[right]

            if not leftvalue.isalnum():
                left = left + 1
            
            if not rightvalue.isalnum():
                right = right - 1

            if leftvalue.isalnum() and rightvalue.isalnum() and not leftvalue.lower() == rightvalue.lower():
                return False

            elif leftvalue.isalnum() and rightvalue.isalnum() and leftvalue.lower() == rightvalue.lower():
                left = left + 1
                right = right - 1
        
        return True