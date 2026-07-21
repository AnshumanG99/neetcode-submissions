class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l = 0
        r = 0

        targetchar = {}
        curchar = {}

        curmatch = 0
        maxlen = len(s) + 1
        maxl = 0
        minr = 0

        for value in t:
            targetchar[value] = targetchar.get(value, 0) + 1

        while r < len(s):
            if s[r] in targetchar:
                curchar[s[r]] = curchar.get(s[r], 0) + 1

                if curchar[s[r]] <= targetchar[s[r]]:
                    curmatch += 1

            r += 1

            while curmatch == len(t):
                if (len(s[l:r]) < maxlen):
                    maxl = l
                    minr = r
                    maxlen = len(s[l:r])

                if s[l] in targetchar:
                    curchar[s[l]] = curchar.get(s[l], 0) - 1

                    if curchar[s[l]] < targetchar[s[l]]:
                        curmatch -= 1

                l += 1

        return s[maxl:minr]
