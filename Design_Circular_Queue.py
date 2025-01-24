class MyCircularQueue:

    def __init__(self, k: int):
        self.s = k
        self.q= [None] *k
        self.f = -1
        self.r = -1
        

    def enQueue(self, value: int) -> bool:
        if(None in self.q):
        
            if(self.f ==-1):
                self.f =0 % self.s
            
            self.r  = (self.r +1)%self.s
            self.q[self.r] = value
            return True
        else:
            return False
        

    def deQueue(self) -> bool:
        if(self.q.count(None)==self.s):
            return False
        else:

            if(self.f == self.r):
                self.r =-1
                self.f = -1
                self.q = [None] * self.s
                return True
            self.q[self.f] = None
            self.f = (self.f +1) %self.s
            
            return True


        

    def Front(self) -> int:
        if(self.q.count(None)==self.s):
            return -1
        return self.q[self.f]
        

    def Rear(self) -> int:
        if(self.q.count(None)==self.s):
            return -1
        return self.q[self.r]
        

    def isEmpty(self) -> bool:
        if(self.q.count(None)==self.s):
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if(None not in self.q):
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
