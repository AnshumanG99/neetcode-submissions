class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l = 0
        r = 0
        count1 = [0] * 26
        count2 = [0] * 26

        for value in s1:
            bucket = ord(value) - ord('a')
            count1[bucket] = count1[bucket] + 1
        
        while r < len(s2):

            curvalue = ord(s2[r]) - ord('a') 
            count2[curvalue] = count2[curvalue] + 1
            
            if r > len(s1) - 1:
                leftvalue = ord(s2[l]) - ord('a') 
                count2[leftvalue] = count2[leftvalue] - 1
                l += 1

            if count2 == count1:
                return True

            r += 1

        return False
                        