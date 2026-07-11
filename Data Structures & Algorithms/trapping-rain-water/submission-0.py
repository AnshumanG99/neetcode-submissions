class Solution:
    def trap(self, height: List[int]) -> int:
        
        prefix = []
        suffix = []
        volume = 0

        lmax = 0
        rmax = 0

        for i in range(len(height)):
            prefix.append(lmax)
            suffix.insert(0, rmax)

            if height[i] > lmax:
                lmax = height[i]
            if height[len(height) - 1 - i] > rmax:
                rmax = height[len(height) - 1 - i]

        for i in range(len(height)):
            position = min(suffix[i], prefix[i]) - height[i]
            if position > 0:
                volume += position

        return volume



            
            

            

