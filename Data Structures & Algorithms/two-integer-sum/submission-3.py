class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seendict = {}

        for i in range(len(nums)):

            if target - nums[i] in seendict:
                return [seendict[target-nums[i]], i]
            
            seendict[nums[i]] = i
        
        