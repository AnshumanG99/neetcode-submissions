class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""

        for value in strs:
            encoded = encoded + str(len(value)) + "#" + value
        
        return encoded

    def decode(self, s: str) -> List[str]:

        i = 0
        answer = []
        prevread = 0
        readlen = 0


        while i < len(s):
    
            if s[i] == "#":
                readlen = int(s[prevread:i])
                answer.append(s[i+1:readlen+i+1])
                prevread = i + readlen + 1
                i = i + readlen + 1
            else:
                i += 1
                
        return answer
            
                
            
        

