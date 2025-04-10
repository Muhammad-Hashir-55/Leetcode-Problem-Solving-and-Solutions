class MyCircularDeque:

    def __init__(self, k: int):
     
        self.d = []
        self.s = k
        

    def insertFront(self, value: int) -> bool:
        if(len(self.d)<self.s):
            self.d.insert(0,value)
            return True
        else:
            return False
        

    def insertLast(self, value: int) -> bool:
        if(len(self.d)<self.s):
            self.d.append(value)
            return True
        else:
            return False
        

    def deleteFront(self) -> bool:
        if(not self.d):
            return False
        else:
            self.d.pop(0)
            return True
        

    def deleteLast(self) -> bool:
        if(not self.d):
            return False
        else:
            self.d.pop()
            return True
        

    def getFront(self) -> int:
        if(not self.d):
            return -1
        else:
            return self.d[0]
        

    def getRear(self) -> int:
        if(not self.d):
            return -1
        else:
            return self.d[-1]
        
    def isEmpty(self) -> bool:
        if(not self.d):
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if(len(self.d)==self.s):
            return True
        else:
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
