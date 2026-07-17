class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0 
        r = len(nums) - 1

        while l < r:

            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            
            else:
                r = mid
        
        if target == nums[l]:
            return l
        
        elif target <= nums[-1]:
            r = len(nums) - 1
        
        else:
            r = l
            l = 0
        
        while l <= r:

            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
            
        return -1