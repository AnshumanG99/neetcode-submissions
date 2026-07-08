class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ordered = set(nums)
        orderedarray = list(ordered)
        possiblenums = []

        for i in range(len(orderedarray)):
            if not (orderedarray[i]-1) in ordered:
                possiblenums.append(orderedarray[i])
        
        maxlen = 0
        curlen = 1

        for i in range(len(possiblenums)):
            curnum = possiblenums[i]
            isSearching = True

            while isSearching:
                if (curnum+1) in ordered:
                    curnum = curnum + 1
                    curlen = curlen + 1

                else:
                    isSearching = False
                    curlen = 1

                if curlen > maxlen:
                    maxlen = curlen

        return maxlen
