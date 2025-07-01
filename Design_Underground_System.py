class UndergroundSystem:

    def __init__(self):
        self.check_in_data = {}
        self.trip = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_data[id] = [stationName ,t]

        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        sta , old_t = self.check_in_data[id]
        tot = t - old_t
        key = (sta , stationName)
        if(key not in self.trip):
            self.trip[key] = [0,0]
        self.trip[key][0] += tot
        self.trip[key][1] += 1
        del self.check_in_data[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tot , coun = self.trip[(startStation , endStation)]
        return tot / coun
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
