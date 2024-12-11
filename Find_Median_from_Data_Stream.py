class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        

    def findMedian(self) -> float:
        self.arr.sort()
        n=  len(self.arr)
        if(n %2 != 0):
            return self.arr[n//2]
        else:
            ind = n//2
            x = (self.arr[ind] + self.arr[ind -1])/2
            return x
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
