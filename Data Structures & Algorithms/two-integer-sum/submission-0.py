class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        values = {}

        for i in range(len(nums)):
            if (target - nums[i]) in values:
                return [values[target - nums[i]], i]

            if not nums[i] in values:
                values[nums[i]] = i