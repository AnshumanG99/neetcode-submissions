class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        timestack = []
        cars = list(zip(position, speed))
        cars.sort()
        cars = cars[::-1]
        

        for p, s in cars:
            time = (target - p) / s

            if timestack and time <= timestack[-1]:
                time = max(timestack[-1], time)
                timestack.pop()

            timestack.append(time)

        return len(timestack)
            



