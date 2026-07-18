class Solution:
    def trap(self, height: List[int]) -> int:
        
        prefix = []
        suffix = []

        answer = 0

        lmax = 0
        rmax = 0

        for i in range(len(height)):

            prefix.append(lmax)
            suffix.insert(0, rmax)

            if height[i] > lmax:
                lmax = height[i]
            
            if height[len(height) - i - 1] > rmax:
                rmax = height[len(height) - i - 1]
            
    
        for i in range(len(height)):

            curheight = height[i]
            volume = min(prefix[i], suffix[i]) - height[i]

            if volume > 0:
                answer += volume
        
        return answer

            