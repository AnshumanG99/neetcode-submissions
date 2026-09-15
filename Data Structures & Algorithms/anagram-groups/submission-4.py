class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        values = {}
        answer = []

        for value in strs:
            
            valuesdict = [0] * 26

            for i in range(len(value)):
                charindex = ord(value[i]) - ord('a')
                valuesdict[charindex] +=1
                
            
            valuesdict = tuple(valuesdict)
            
            if valuesdict in values:
                values[valuesdict].append(value)
            else:
                values[valuesdict] = [value]
            
        
        for key, value in values.items():
            answer.append(value)
    
        return answer
