class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.ptr = 0
        self.li = [0]*n
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.li[idKey-1] = value
        temp = []
        st = self.ptr
        for i in range(st,self.n):
            if(self.li[i] == 0):
                break
            temp.append(self.li[i])
            self.ptr +=1
        return temp

        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
