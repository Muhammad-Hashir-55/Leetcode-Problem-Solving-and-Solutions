class Solution:
    def countKeyChanges(self, s: str) -> int:
        ns = ''
        for i in s:
            ns += i.lower()
        last = ''
        ss = set()
        change = 0
        for i in ns:
            if(not ss):
                ss.add(i)
                last = i
            elif(i not in ss):
                ss.add(i)
                change +=1
                last = i
            elif(i in ss and last != i):
                change +=1
                ss.add(i)
                last = i
            last = i
        return change
            
        
