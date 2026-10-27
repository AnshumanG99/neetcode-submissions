class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        valueset = set(nums)
        curstreak = 1
        maxstreak = 0
        
        for value in nums:

            if not (value - 1) in valueset:
                while value + 1 in valueset:
                    curstreak += 1
                    value = value + 1

                    
            if curstreak > maxstreak:
                maxstreak = curstreak
                
            curstreak = 1
            
        return maxstreak