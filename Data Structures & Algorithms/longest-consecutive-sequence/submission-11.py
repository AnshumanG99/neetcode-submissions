class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numsset = set(nums)

        answer = 0

        for value in numsset:

            if (value - 1) not in numsset:
                length = 1

                while (value + length) in numsset:
                    length += 1
                
                if length > answer:
                    answer = length
        
        return answer