class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        answer = right

        while left <= right:

            eatspeed = (left + right) // 2
            time = 0

            for value in piles:
                time += math.ceil(value / eatspeed)
            
            if time > h:
                left = eatspeed + 1
            else:
                if eatspeed < answer:
                    answer = eatspeed
                right = eatspeed - 1

        return answer