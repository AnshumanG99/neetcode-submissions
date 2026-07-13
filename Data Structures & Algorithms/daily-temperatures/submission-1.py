class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        tempstack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            
            value = temperatures[i]
            
            while tempstack and value > temperatures[tempstack[-1]]:
                result[tempstack[-1]] = i - tempstack[-1]
                tempstack.pop()
            
            if tempstack and value <= temperatures[tempstack[-1]] or not tempstack:
                tempstack.append(i)

        return result
