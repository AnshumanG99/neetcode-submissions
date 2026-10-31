class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        valstack = []
        operators = {"*", "/", "+", "-"}


        for value in tokens:
            if not value in operators:
                valstack.append(value)
            
            else:
                val1 = int(valstack.pop())
                val2 = int(valstack.pop())

                if value == "+":
                    valstack.append(val1 + val2)
                
                elif value == "*":
                    valstack.append(val1 * val2)
                
                elif value == "-":
                    valstack.append(val2 - val1)
                
                elif value == "/":
                    valstack.append(val2 / val1)
        
        return int(valstack[0])