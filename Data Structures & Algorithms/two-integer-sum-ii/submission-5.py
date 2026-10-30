class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        head = 0 
        tail = len(numbers) - 1

        while head < tail:
            
            currsum = numbers[head] + numbers[tail]

            if currsum > target:
                tail -= 1
            
            elif currsum < target:
                head += 1
            
            else:
                return [head + 1, tail + 1]
        
        return []