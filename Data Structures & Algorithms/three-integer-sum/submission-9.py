class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        answerset = []
        nums.sort()

        for i in range(len(nums) - 2):
            head = i + 1
            tail = len(nums) - 1
            target = 0 - nums[i]

            if i > 0 and nums[i] == nums[i - 1]:
                continue 
                
            while head < tail:

                cursum = nums[head] + nums[tail]

                if cursum > target: 
                    tail -= 1
                
                elif cursum < target:
                    head += 1
                
                else:
                    answerset.append([nums[i], nums[head], nums[tail]])
                    head += 1
                    tail -= 1
                    while head < tail and nums[head] == nums[head - 1]:
                        head += 1
                

            
        return answerset


