class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        answer = [0] * len(nums)

        for i in range(len(nums)):
            
            if i >= 1:
                prefix[i] = prefix[i-1] * nums[i-1]
                suffix[len(nums) - i - 1] = suffix[len(nums) - i] * nums[len(nums) - i]
            
            else:
                prefix[i] = 1
                suffix[len(nums) - i - 1] = 1
            
        
        for i in range(len(nums)):
            answer[i] = prefix[i] * suffix[i]
        
        return answer