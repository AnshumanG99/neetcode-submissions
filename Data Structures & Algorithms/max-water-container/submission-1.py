class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        curmax = 0

        while left < right: 

            width = right - left
            leftval = heights[left]
            rightval = heights[right]
            height = min(leftval, rightval)
            volume = width * height

            if volume > curmax:
                curmax = volume
            
            if height == leftval:
                left = left + 1
            
            if height == rightval:
                right = right - 1
        
        return curmax

            