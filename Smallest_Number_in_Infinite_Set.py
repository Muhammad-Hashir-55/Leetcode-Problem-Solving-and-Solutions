class SmallestInfiniteSet:

    def __init__(self):
        self.s = set()
        for i in range(1,1001):
            self.s.add(i)
        

        

    def popSmallest(self) -> int:
        mini = 999999
        for i in self.s:
            if(i <mini):
                mini = i
        self.s.remove(mini)
        return mini

        
        

    def addBack(self, num: int) -> None:
        self.s.add(num)
        
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
