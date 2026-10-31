class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l, r = 0, 0
        
        charfreq = {}
        maxlen = 0

        while r < len(s):
            
            if s[r] in charfreq:
                charfreq[s[r]] += 1
            else:
                charfreq[s[r]] = 1

            r+= 1

            while r - l > max(charfreq.values()) + k:
                charfreq[s[l]] -= 1
                l += 1
            
            if r - l > maxlen:
                maxlen = r - l 
            
        
        return maxlen
                
        