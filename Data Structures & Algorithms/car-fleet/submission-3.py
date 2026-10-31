class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        timestack = []
        
        cars = {}

        for i in range(len(position)):
            cars[position[i]] = speed[i]
        
        cars = dict(sorted(cars.items(), reverse = True))
        

        for position, speed in cars.items():
            time = (target - position) / speed

            if timestack and time <= timestack[-1]:
                continue
            else:
                timestack.append(time)
        
        
        return len(timestack)

        