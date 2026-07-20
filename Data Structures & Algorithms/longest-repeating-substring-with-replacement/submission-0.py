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
                charfreq[curvalue] = charfreq[curvalue] + 1

            else:
                charfreq[curvalue] = 1

            if charfreq[curvalue] > maxfreq:
                maxfreq = charfreq[curvalue]

            while (r - l + 1)  > (k + maxfreq) and l < r:
                lastvalue = s[l]
                charfreq[lastvalue] = charfreq[lastvalue] - 1
                l += 1
                
            curlen = r - l + 1

            if curlen > maxlen:
                maxlen = curlen
                
            r += 1

        return maxlen
            