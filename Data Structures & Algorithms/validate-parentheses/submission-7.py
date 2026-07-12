class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {"(" : ")", "{" : "}", "[" : "]"}
        validstack = []
        
        for value in s:
            
            if value in brackets:
                validstack.append(value)
            
            else:
                if validstack and value == brackets[validstack[-1]]:
                    validstack.pop()
                else:
                    return False
            

        return not validstack