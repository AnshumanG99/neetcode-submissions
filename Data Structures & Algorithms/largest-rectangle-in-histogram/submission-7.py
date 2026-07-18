class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heightstack = []
        answer = 0
        heights.append(0)

        for i in range(len(heights)):

            h = heights[i]
            rightboundary = i

            while heightstack and h < heights[heightstack[-1]]:
                
                curheight = heights[heightstack.pop()]

                if heightstack:
                    leftboundary = heightstack[-1]
                else:
                    leftboundary = -1 

                curarea = (rightboundary - leftboundary - 1) * curheight

                if curarea > answer:
                    answer = curarea
                
            heightstack.append(i)
        
        return answer