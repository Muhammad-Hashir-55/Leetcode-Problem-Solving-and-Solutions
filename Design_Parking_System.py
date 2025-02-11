class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.b = [0] * big
        self.m = [0] * medium
        self.s = [0] * small
        

    def addCar(self, carType: int) -> bool:
        if(carType ==1):
            if(self.b):
                self.b.pop()
                return True
            else:
                return False
        elif(carType == 2):
            if(self.m):
                self.m.pop()
                return True
            else:
                return False
        else:
            if(self.s):
                self.s.pop()
                return True
            else:
                return False

        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
