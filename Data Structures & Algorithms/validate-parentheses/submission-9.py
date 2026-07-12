class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {")" : "(" , "]" : "[" , "}" : "{"}
        validstack = []
        
        for value in s:
            if not value in brackets:
                validstack.append(value)
            else:
                if validstack and brackets[value] == validstack[-1]:
                    validstack.pop()
                else:
                    return False
        
        return not validstack