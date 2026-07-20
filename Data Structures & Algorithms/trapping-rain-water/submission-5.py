class Solution:
    def trap(self, height: List[int]) -> int:
        
        prefix = []
        suffix = []

        tvolume = 0

        lmax = 0
        rmax = 0

        for i in range(len(height)):

            prefix.append(lmax)
            suffix.insert(0, rmax)

            if lmax < height[i]:
                lmax = height[i]
            
            if rmax < height[len(height) - i - 1]:
                rmax = height[len(height) - i - 1]
            
        
        for i in range(len(height)):

            curvalue = min(prefix[i], suffix[i]) - height[i]

            if curvalue > 0:
                tvolume += curvalue
        
        return tvolume