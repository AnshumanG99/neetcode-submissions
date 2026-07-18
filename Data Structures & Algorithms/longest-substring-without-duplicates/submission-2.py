class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0
        maxsubstring = 0
        cursubstring = 0
        characterlist = set()

        while r < len(s):
            
            while s[r] in characterlist:
                characterlist.discard(s[l])   
                l += 1
                cursubstring -= 1

            characterlist.add(s[r])
            cursubstring += 1
            r += 1
        
            if cursubstring > maxsubstring:
                maxsubstring = cursubstring

        return maxsubstring