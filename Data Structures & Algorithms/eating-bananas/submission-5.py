class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        answer = r

        while l <= r:

            mides = (l + r) // 2
            time = 0

            for value in piles:
                time += math.ceil(value / mides)
            
            if time > h: 
                l = mides + 1
            
            else:
                if mides < answer:
                    answer = mides
                r = mides - 1
            
        return answer