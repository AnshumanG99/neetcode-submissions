class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        minspeed = r

        while l <= r:

            mid = (l + r) // 2
            eattime = 0

            for value in piles:
                eattime += math.ceil(value / mid)
            
            if eattime <= h:
                minspeed = min(minspeed, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return minspeed