class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        r = 0

        charfreq = {}
        maxfreq = 0

        maxlen = 0

        while r < len(s):
            
            curvalue = s[r]

            if curvalue in charfreq:
                charfreq[curvalue] += 1
            else:
                charfreq[curvalue] = 1
            
            r += 1

            maxfreq = max(charfreq.values())
            
            while (r - l) > (k + maxfreq):    
                lastvalue = s[l]
                charfreq[lastvalue] -= 1
                l += 1
            
            curlen = r - l

            if curlen > maxlen:
                maxlen = curlen
        
        return maxlen