class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        incheight = []
        maxarea = 0

        heights.append(0)

        for i in range(len(heights)):

            value = heights[i]

            while incheight and value < heights[incheight[-1]]:
                currheight = heights[incheight.pop()]
                rightboundary = i
                if incheight: 
                    leftboundary = incheight[-1]
                else:
                    leftboundary = -1
                    
                area = (rightboundary - leftboundary - 1) * currheight

                if area > maxarea: 
                    maxarea = area
            
            incheight.append(i)
        
        return maxarea










        # answer = [0] * len(heights)

        # for i in range(len(heights)):
        #     height = heights[i]
        #     answer[i] = height
        #     currheight = height

        #     for j in range(i, len(heights)):
        #         if heights[j] < currheight:
        #             currheight = heights[j]

        #         area = currheight * (j - i + 1)

        #         if area > answer[i]:
        #             answer[i] = area

        # currmaxarea = 0

        # for value in answer:
        #     if value > currmaxarea:
        #         currmaxarea = value

        # return currmaxarea
