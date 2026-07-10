class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        fix = 0
        answer = []

        while fix < len(nums) - 2:
            
            if fix > 0 and nums[fix] == nums[fix - 1]:
                fix += 1
                continue

            left = fix + 1
            right = len(nums) - 1

            while left < right:
                target = -nums[fix]
                if nums[left] + nums[right] > target:
                    right = right - 1
                elif nums[left] + nums[right] < target:
                    left = left + 1
                else: 
                    answer.append([nums[fix], nums[left], nums[right]])
                    left = left + 1
                    right = right - 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

            fix = fix + 1

        return answer
            