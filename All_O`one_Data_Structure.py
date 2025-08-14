class AllOne:

    def __init__(self):
        self.dic = {}
        
        
        

    def inc(self, key: str) -> None:
        if(key not in self.dic):
            self.dic[key] = 1
            
        else:
            self.dic[key] +=1
            
        
        

    def dec(self, key: str) -> None:
        self.dic[key] -=1
        if(self.dic[key] == 0):
            del self.dic[key]



        

    def getMaxKey(self) -> str:
        if(not self.dic):
            return ''
        maxi = max(self.dic.values())
        for i in self.dic:
            if(self.dic[i] == maxi):
                return i
        
        

    def getMinKey(self) -> str:
        if(not self.dic):
            return ''
        mini = min(self.dic.values())
        for i in self.dic:
            if(mini == self.dic[i]):
                return i
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
