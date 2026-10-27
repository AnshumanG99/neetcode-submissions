class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if not len(s) == len(t):
            return False

        characters1 = [0] * 26
        characters2 = [0] * 26

        for i in range(len(s)):
            characters1[ord(s[i]) - ord('a')] += 1
            characters2[ord(t[i]) - ord('a')] += 1
                
        return characters1 == characters2