class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        r = 0

        characters = set()

        long = 0
        cur = 0

        while r < len(s):

            while s[r] in characters:
                characters.discard(s[l])
                cur -= 1
                l += 1

            characters.add(s[r])
            cur += 1
            r += 1

            if cur > long:
                long = cur

        return long
