class Trie:

    def __init__(self):
        self.ss = set()
        

    def insert(self, word: str) -> None:
        self.ss.add(word)
    

    def search(self, word: str) -> bool:
        if(word in self.ss):
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        for i in self.ss:
            if(prefix in i):
                idx = i.index(prefix)
                if(idx == 0):
                    return True
        return False
                
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
