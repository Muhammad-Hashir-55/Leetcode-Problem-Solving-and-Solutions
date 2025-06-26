from sortedcontainers import SortedSet

class NumberContainers:

    def __init__(self):
        self.dic = {}
        self.nums = []
        self.oth = {}
        

    def change(self, index: int, number: int) -> None:
        if(number not in self.dic):
            self.dic[number] = SortedSet()
            self.dic[number].add(index)
        else:
            self.dic[number].add(index)
        
        if(index in self.oth):
            if(self.oth[index] != number):
                self.dic[self.oth[index]].discard(index)
                    
        self.oth[index] = number

        
        
        
        

    def find(self, number: int) -> int:
        if(number not in self.dic or not self.dic[number] ):
            return -1
        return (self.dic[number][0])
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
