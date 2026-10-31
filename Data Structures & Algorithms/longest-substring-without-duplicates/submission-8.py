class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, r = 0, 0

        subset = set()
        maxsub = 0

        while r < len(s):
            
            while r < len(s) and s[r] not in subset :
                subset.add(s[r])
                r += 1
            
            maxsub = max(r - l, maxsub)
            subset.remove(s[l])
            l += 1
        
        return maxsub
            