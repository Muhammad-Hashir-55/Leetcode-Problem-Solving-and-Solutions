import random
class RandomizedSet:

    def __init__(self):
        self.s = set()
        

    def insert(self, val: int) -> bool:
        if(val not in self.s):
            self.s.add(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if(val in self.s):
            self.s.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        arr =[]
        for i in self.s:
            arr.append(i)
        x = random.choices(arr)
        
        return x[0]
        # for i in self.s:
        #     return i
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
