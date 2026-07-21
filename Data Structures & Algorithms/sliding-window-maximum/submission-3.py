class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        r = 0
        maxarray = []
        curmax = float('-inf')

        while r < len(nums):
            
            if nums[r] > curmax:
                curmax = nums[r]

            if r >= k - 1:
                maxarray.append(curmax)

                if nums[r - k + 1] >= curmax:
                    curmax = float('-inf')

                    for j in range(k - 1):
                        if nums[r - j] >= curmax:
                            curmax = nums[r-j]
                
            r += 1
    
        return maxarray
                