class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1

        while left < right:

            leftvalue = numbers[left]
            rightvalue = numbers[right]

            if leftvalue + rightvalue > target:
                right = right - 1
            elif leftvalue + rightvalue < target:
                left = left + 1
            else:
                return [left + 1, right + 1]
            