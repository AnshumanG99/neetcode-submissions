class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, r = 0, 0

        seenmap = set()
        longstring = 0

        while r < len(s):
            
            while seenmap and s[r] in seenmap:
                seenmap.remove(s[l])
                l += 1

            longstring = max(longstring, r - l + 1)
            seenmap.add(s[r])
            r += 1
        
        return longstring