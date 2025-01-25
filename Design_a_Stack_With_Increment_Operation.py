class CustomStack:

    def __init__(self, maxSize: int):
        self.s = maxSize
        self.st = []
        

    def push(self, x: int) -> None:
        if(len(self.st)<self.s):
            self.st.append(x)
            return
        

    def pop(self) -> int:
        if(not self.st):
            return -1
        else:
            x = self.st[-1]
            self.st.pop()
            return x
        

    def increment(self, k: int, val: int) -> None:
        n =len(self.st)
        i =0
        while(i<k):
            if(i ==n):
                break
            self.st[i] +=val
            i +=1
            
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
