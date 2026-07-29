class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numsset = set(nums)
        incrementednums = list(numsset)
        incrementednums.sort()

        answer = 0
        curseq = 1

        print(incrementednums)

        for i in range(len(incrementednums)):

            if i > 0 and incrementednums[i] == (incrementednums[i-1] + 1):
                print(incrementednums[i])
                curseq = curseq + 1
            
            else:
                curseq = 1
            
            if curseq > answer:
                answer = curseq                
        
        return answer