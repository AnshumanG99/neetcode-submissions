class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l < r: 

            mid = (l + r) // 2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        pivot = l
        r = len(nums) - 1
        
        if target >= nums[pivot] and target <= nums[r]:
            r = len(nums) - 1
        else:
            r = pivot - 1
            pivot = 0
            
        while pivot <= r:

            mid = (pivot + r) // 2

            if nums[mid] > target:
                r = mid - 1
            if nums[mid] < target:
                pivot = mid + 1
            if nums[mid] == target:
                return mid

        return -1

                