class MyStack:

    def __init__(self):
        self.q= []
        

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        x = self.q[-1]
        self.q.pop()
        return x
        

    def top(self) -> int:
        return self.q[-1]
        

    def empty(self) -> bool:
        if(self.q ==[]):
            return True
        else:
            return False

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
