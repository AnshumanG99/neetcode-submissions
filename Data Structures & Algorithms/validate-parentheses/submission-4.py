class Solution:
    def isValid(self, s: str) -> bool:
        
        check = []
        brackets = {")" : "(", "}" : "{" , "]" : "["}

        for value in s:

            if not value in brackets:
                check.insert(0, value)

            if value in brackets:
                if len(check) > 0 and brackets[value] == check[0]:
                    check.pop(0)
                else:
                    return False
        
            
        if len(check) > 0:
            return False

        return True

