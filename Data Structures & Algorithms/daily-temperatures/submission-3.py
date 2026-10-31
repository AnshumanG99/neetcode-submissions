class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        seentemps = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            
            value = temperatures[i]

            while seentemps and value > temperatures[seentemps[-1]]:
                result[seentemps[-1]] = i - seentemps[-1]
                seentemps.pop()
            
            seentemps.append(i)
        
        return result

        