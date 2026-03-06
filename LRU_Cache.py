class LRUCache:

    def __init__(self, capacity: int):
        self.lru = []
        self.dic = {}
        self.n = capacity
        

    def get(self, key: int) -> int:

        if(key in self.dic):
            self.lru.remove(key)
            self.lru.insert(0,key)
            return self.dic[key]
            
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if(key in self.dic):
            self.lru.remove(key)
        elif(len(self.dic) == self.n):
            old = self.lru.pop()
            del self.dic[old]
        self.dic[key] = value
        self.lru.insert(0,key)




        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
