class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        order = []
        operators = {"+", "-", "*", "/", }
        total = 0

        for value in tokens:
            
            answer = 0

            if not value in operators:
                order.append(int(value))
            
            if value in operators:
    
                if value == "+":
                    answer = order[-2] + order[-1]
                if value == "-":
                    answer = order[-2] - order[-1]
                if value == "*":
                    answer = order[-2] * order[-1]
                if value == "/":
                    answer = int(order[-2] / order[-1])
                
                order.pop()
                order.pop()
                order.append(answer)
        
        return order[-1]
