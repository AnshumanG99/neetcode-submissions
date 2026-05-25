class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        indexes = set()
        for num in nums:
            if num in indexes:
                return True
            indexes.add(num)
            
        return False
