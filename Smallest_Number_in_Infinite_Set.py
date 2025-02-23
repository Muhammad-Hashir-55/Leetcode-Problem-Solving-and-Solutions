class SmallestInfiniteSet:

    def __init__(self):
        self.s = set()
        smallest = 1

        

    def popSmallest(self) -> int:
        a = -1
        i = 1
        while(True):
            if(i not in self.s):
                a = i
                break
            i +=1
        self.s.add(a)
        return a

        

    def addBack(self, num: int) -> None:
        if(num in self.s):
            self.s.remove(num)
        
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
