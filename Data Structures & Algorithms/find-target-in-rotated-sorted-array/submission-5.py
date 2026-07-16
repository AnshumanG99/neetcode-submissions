class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        pivot = 0

        while l < r:

            mid = (l + r) // 2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        pivot = l

        if target <= nums[-1]:
            l = pivot
            r = len(nums) - 1
        else:
            l = 0
            r = pivot

        while l <= r :

            mid = (l + r) // 2
            
            if nums[mid] == target: 
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1 