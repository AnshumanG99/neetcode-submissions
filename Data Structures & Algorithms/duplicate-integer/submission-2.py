class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        indexes = {}
        for i in range (len(nums)):
            if not nums[i] in indexes:
                indexes[nums[i]] = i
            else:
                return True
            
        return False
