class Solution:

    def encode(self, strs: List[str]) -> str:

        finalstring = ""

        for value in strs:
            
            finalstring += str(len(value)) + "#" + value
        
        return finalstring

    def decode(self, s: str) -> List[str]:
        
        answer = []
        curread = ""
        readval = 0
        i = 0

        while i < len(s):
            if not s[i] == "#":
                curread += s[i] 
                i += 1

            else:
                readval = int(curread)
                answer.append(s[i + 1: i + readval + 1])
                i += readval + 1
                curread = ""
                readval = 0

        return answer