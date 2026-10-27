class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        numsset = set()
        for value in nums:
            if value in numsset:
                return True
            
            numsset.add(value)
        
        return False