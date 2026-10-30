class Solution:
    def maxArea(self, heights: List[int]) -> int:

        head = 0
        tail = len(heights) - 1
        maxarea = 0

        while head < tail:
            curarea = min(heights[head], heights[tail]) * (tail - head) 

            if curarea > maxarea: 
                maxarea = curarea
            
            if min(heights[head], heights[tail]) == heights[tail]:
                tail -= 1
            else:
                head += 1
        
        return maxarea

        