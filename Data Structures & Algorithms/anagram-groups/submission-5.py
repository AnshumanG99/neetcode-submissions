class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seendict = {}
        answer = []

        for value in strs:
            
            valuechar = [0] * 26

            for i in range(len(value)):
                valuechar[ord(value[i]) - ord('a')] += 1
            
            valtuple = tuple(valuechar)

            if valtuple in seendict:
                seendict[valtuple].append(value)

            else:
                seendict[valtuple] = [value]

        for key, items in seendict.items():
            answer.append(items)

        return answer