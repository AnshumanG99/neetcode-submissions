class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        hstack = []
        greatestarea = 0
        heights.append(0)

        for i in range(len(heights)):
            
            curval = heights[i]

            while hstack and curval < heights[hstack[-1]]:

                height = heights[hstack.pop()]
                rboundary = i

                if hstack:
                    lboundary = hstack[-1]
                else:
                    lboundary = -1
                
                curarea = (rboundary - lboundary - 1) * height

                if curarea > greatestarea:
                    greatestarea = curarea
            
            hstack.append(i)
            
        return greatestarea

                