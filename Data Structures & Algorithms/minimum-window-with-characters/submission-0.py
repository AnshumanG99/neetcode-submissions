class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l = 0
        r = 0

        targetchar = {}
        curchar = {}
        matchcharacters = 0
        minlen = len(s)
        minl, minr = 0, 0

        for value in t:
            if value in targetchar:
                targetchar[value] += 1
            else:
                targetchar[value] = 1

        while r < len(s):
            if s[r] in targetchar:
                if s[r] in curchar:
                    curchar[s[r]] += 1

                else:
                    curchar[s[r]] = 1

                if curchar[s[r]] <= targetchar[s[r]]:
                    matchcharacters += 1

            r += 1

            while matchcharacters == len(t):
                leftval = s[l]
                substring = s[l:r]

                if len(substring) <= minlen:
                    minlen = len(substring)
                    minl, minr = l, r

                if leftval in targetchar:
                    curchar[leftval] -= 1

                    if curchar[leftval] < targetchar[leftval]:
                        matchcharacters -= 1

                l += 1

        return s[minl:minr]
