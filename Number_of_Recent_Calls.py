class RecentCounter:

    def __init__(self):
        self.st = 0
        self.rang = []
        

    def ping(self, t: int) -> int:
        self.rang.append(t)
        while(self.rang[self.st] < (t-3000)):
            self.st +=1
        return len(self.rang) - self.st


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
