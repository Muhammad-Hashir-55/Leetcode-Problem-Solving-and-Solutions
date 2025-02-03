class FrontMiddleBackQueue:

    def __init__(self):
        self.q =[]
        

    def pushFront(self, val: int) -> None:
        self.q.insert(0,val)
        

    def pushMiddle(self, val: int) -> None:
        if(not self.q):
            self.q.append(val)
        else:
            n = len(self.q)
            i =n//2
            self.q.insert(i,val)
            print(self.q)
        

        

    def pushBack(self, val: int) -> None:
        self.q.append(val)
        

    def popFront(self) -> int:
        if(not self.q):
            return -1
        
        x = self.q[0]
        self.q.pop(0)
        return x
        

    def popMiddle(self) -> int:
        if(not self.q):
            return -1
        n = len(self.q)
        decr = False
        if(n %2 ==0):
            decr = True

        
        i = n//2
        if(decr == True):
            i -=1

        x = self.q[i]
        
        self.q.pop(i)
        return x
        

    def popBack(self) -> int:
        if(not self.q):
            return -1
        else:
            x = self.q[-1]
            self.q.pop()
            return x
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
