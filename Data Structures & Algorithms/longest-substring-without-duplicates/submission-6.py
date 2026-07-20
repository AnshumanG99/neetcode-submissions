class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0

        characterlist = set()

        maxlen = 0

        while r < len(s):


            while s[r] in characterlist:
                characterlist.remove(s[l])
                l += 1
            
            characterlist.add(s[r])
            r += 1
        
            curlen = r - l

            if curlen > maxlen:
                maxlen = curlen
        
        return maxlen
        
        
