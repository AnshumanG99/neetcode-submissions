class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        hstack = []
        answer = 0
        heights.append(0)

        for i in range(len(heights)):

            height = heights[i]
            rightboundary = i
            

            while hstack and height < heights[hstack[-1]]:

                curheight = heights[hstack.pop()]

                if hstack:
                    leftboundary = hstack[-1]
                else:
                    leftboundary = -1
            
                curarea = curheight * (rightboundary - leftboundary - 1)

                if curarea > answer:
                    answer = curarea
            
            hstack.append(i)
            
        
        return answer