class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        indexes = set()
        for i in range (len(nums)):
            if not nums[i] in indexes:
                indexes.add(nums[i])
            else:
                return True
            
        return False
