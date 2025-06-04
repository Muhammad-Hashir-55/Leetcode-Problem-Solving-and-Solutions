class TimeMap:

    def __init__(self):
        self.dic = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key not in self.dic):
            self.dic[key] = []
        self.dic[key].append((timestamp , value))

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ''
        
        arr = self.dic[key]
        low, high = 0, len(arr) - 1
        res = '' 

        while low <= high:
            mid = (low + high) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]    
                low = mid + 1        
            else:
                high = mid - 1        

        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
