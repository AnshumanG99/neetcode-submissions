class TimeMap:

    def __init__(self):
        
        self.valuemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if not key in self.valuemap:
            self.valuemap[key] = [[timestamp, value]]
        else:
            self.valuemap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        
        if not key in self.valuemap:
            return ""
            
        l = 0 
        r = len(self.valuemap[key]) - 1
        answer = -1

        while l <= r:
            
            mid = (l + r) // 2
            currvalue = self.valuemap[key]

            if currvalue[mid][0] > timestamp: 
                r = mid - 1
            
            else:
                if currvalue[mid][0] <= timestamp:
                    answer = mid
                    l = mid + 1
        
        if answer >= 0:
            return currvalue[answer][1]

        return ""                
            