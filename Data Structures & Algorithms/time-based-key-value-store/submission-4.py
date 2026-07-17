class TimeMap:

    def __init__(self):
        
        self.valuemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key in self.valuemap:
            self.valuemap[key].append([value, timestamp])
        
        else:
            self.valuemap[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        
        if not key in self.valuemap:
            return ""
            
        l = 0
        r = len(self.valuemap[key]) - 1
        answer = -1

        while l <= r:

            mid = (l + r) // 2
            currvalue = self.valuemap[key][mid][1]

            if currvalue > timestamp:
                r = mid - 1
            
            else:
                if mid > answer:
                    answer = mid
                l = mid + 1
        
        if answer >= 0:
            return self.valuemap[key][answer][0]
        
        return ""

