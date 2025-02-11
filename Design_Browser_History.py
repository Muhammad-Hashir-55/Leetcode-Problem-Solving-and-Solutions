class BrowserHistory:

    def __init__(self, homepage: str):
        self.s =[homepage]
        self.f = []  # this was good constraint 
        # remember we need to first have empty forward as when object was created nothing was their to forward
        # rest the solution is easy just a little twist in forward function

        

    def visit(self, url: str) -> None:
        self.s.append(url)
        self.f = []
        

    def back(self, steps: int) -> str:
        n = len(self.s)
        ii = 0

        for i in range(n-1):
            if(ii == steps):
                break
            x = self.s.pop()
            self.f.append(x)
            ii +=1
        return self.s[-1]
        

    def forward(self, steps: int) -> str:
        n = len(self.f)
        ii = 0
        
        for i in range(n):
            if(ii == steps):
                break
            x = self.f.pop()
            self.s.append(x)

            ii +=1

        return self.s[-1]
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
