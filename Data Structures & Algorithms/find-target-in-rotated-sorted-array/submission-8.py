class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:
                return mid 
                
            if nums[mid] > target and nums[mid] > nums[r]:
                if target >= nums[l]:
                    r = mid - 1 
                else:
                    l = mid + 1 
            elif nums[mid] > target and nums[mid] < nums[r]:
                r = mid - 1
            else:
                if nums[mid] < nums[r] and target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            
        return -1
            
