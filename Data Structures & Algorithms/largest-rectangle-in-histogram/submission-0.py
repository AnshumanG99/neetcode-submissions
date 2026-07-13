class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        answer = [0] * len(heights)

        for i in range(len(heights)):               
           
            height = heights[i]
            answer[i] = height
            currheight = height

            for j in range(i, len(heights)):
                
                if heights[j] < currheight:
                    currheight = heights[j]
                
                area = currheight * (j - i + 1)

                if area > answer[i]:
                    answer[i] = area
        
        currmaxarea = 0

        for value in answer:
            if value > currmaxarea:
                currmaxarea = value

        return currmaxarea
                