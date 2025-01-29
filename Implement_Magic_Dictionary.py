class MagicDictionary:

    def __init__(self):
        self.arr = []
        

    def buildDict(self, dictionary: List[str]) -> None:
        self.arr = dictionary
        

    def search(self, searchWord: str) -> bool:
        nn = len(searchWord)
        for i in self.arr:
            n = len(i)
            c = 0
            if(n !=nn):
                continue
            

            for j in range(n):
                if(i[j]!= searchWord[j]):
                    c +=1
                if(c>1):
                    break
            if(c ==1):
                return True
        return False

            
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
