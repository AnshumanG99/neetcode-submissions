class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            
            mid = (left + right) // 2

            midvert = mid // len(matrix[0])
            midhori = mid - (midvert * len(matrix[0]))

            if matrix[midvert][midhori] > target:
                right = mid - 1
            elif matrix[midvert][midhori] < target:
                left = mid + 1
            else:
                return True
        
        return False

 
