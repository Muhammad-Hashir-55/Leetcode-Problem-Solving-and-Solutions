class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time = timeToLive
        self.dic = {}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        
        self.dic[tokenId] = currentTime + self.time


        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if(tokenId not in self.dic):
            return
        elif(self.dic[tokenId] <= currentTime):
            return
        else:
            self.dic[tokenId] = currentTime + self.time
        
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for i in self.dic:
            if(self.dic[i] > currentTime):
                count +=1
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
