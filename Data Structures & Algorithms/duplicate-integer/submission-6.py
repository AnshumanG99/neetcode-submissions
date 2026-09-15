class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        indexes = set()

        for value in nums:
            if value in indexes: 
                return True
            
            else:
                indexes.add(value)
            
        return False