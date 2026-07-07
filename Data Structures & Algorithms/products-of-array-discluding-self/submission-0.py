class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        suffix = []
        answer = []

        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
                suffix.insert(0, 1)
            else:
                prefix.append(prefix[i-1] * nums[i-1])
                suffix.insert(0, suffix[0] * nums[len(nums)-i])
        
        for i in range(len(nums)):
            answer.append(prefix[i] * suffix[i])
        
        return answer
        