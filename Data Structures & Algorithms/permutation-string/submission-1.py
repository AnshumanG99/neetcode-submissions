class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l , r = 0 , 0

        d1 = {}
        d2 = {}


        for value in s1:
            if value in d1:
                d1[value] += 1
            else:
                d1[value] = 1
        
        while r < len(s2):

            if s2[r] in d2:
                d2[s2[r]] += 1
            else:
                d2[s2[r]] = 1

            r += 1

            if r - l == len(s1):

                if d1 == d2:
                    return True

                # d1array = []
                # d2array = []
                # for key, value in d1.items():
                #     d1array.append([key, value])
                
                # for key, value in d2.items():
                #     d2array.append([key, value])
                
                # d1array.sort()
                # d2array.sort()

                # if d1array == d2array:
                #     return True
                
                else:
                    d2[s2[l]] -= 1
                    if d2[s2[l]] == 0:
                        d2.pop(s2[l])
                    l += 1
        
        return False
            