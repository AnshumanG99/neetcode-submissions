class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = sorted(s)
        s2 = sorted(t)

        print(s1)
        print(s2)

        return s1 == s2
