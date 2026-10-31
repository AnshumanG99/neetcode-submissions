class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        tempstack = []
        results = [0] * len(temperatures)

        for i in range(len(temperatures)):
            
            value = temperatures[i]

            while tempstack and value > temperatures[tempstack[-1]]:
                results[tempstack[-1]] = i - tempstack[-1]
                tempstack.pop()
            
            tempstack.append(i)
    
        return results