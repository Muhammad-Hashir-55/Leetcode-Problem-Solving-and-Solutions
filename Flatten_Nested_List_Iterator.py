# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        def fl(nested):
            arr= []
            for i in nested:
                
                if(i.isInteger()):
                    arr.append(i.getInteger())
                else:
                    arr.extend(fl(i.getList()))
            return arr
        
        self.fin = fl(nestedList)
        
        self.n = len(self.fin)
        self.idx = 0
        
    
    def next(self) -> int:
        xx =self.fin[self.idx]
        self.idx +=1
        return xx
        
        
    
    def hasNext(self) -> bool:
        if(self.idx < self.n):
            return True
        else:
            return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
