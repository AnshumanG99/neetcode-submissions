class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        answer = r

        while l <= r:

            mid = (l + r) // 2
            midtime = 0

            for value in piles:
                midtime += math.ceil(value / mid)

            if midtime > h: 
                l = mid + 1
            
            else:
                if mid < answer:
                    answer = mid
                r = mid - 1
        
        return answer