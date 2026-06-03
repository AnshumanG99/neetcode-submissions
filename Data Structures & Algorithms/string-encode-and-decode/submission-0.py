class Solution:

    def encode(self, strs: List[str]) -> str:
        
        answer = ""

        for values in strs:
            answer = answer + str(len(values)) + "#" + values

        return answer 

        

    def decode(self, s: str) -> List[str]:

        final = []
        i = 0

        while i < len(s):
            j = i
            while not s[j] == "#":
                j = j + 1

            length = int(s[i:j])

            final.append(s[j + 1: j + 1 + length])

            i = j + 1 + length
    
        return final


            



