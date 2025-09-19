class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        part = s[0]
        idx = 1
        n = len(s)
        arr = []
        while(idx <n):
            icr = False
            for i in part:
                if(i in s[idx:]):
                    icr = True
                    break
            if(icr == True):
                part += s[idx]
                idx +=1
            else:
                arr.append(len(part))
                part = s[idx]
                idx +=1
            
                
        arr.append(len(part))
        return arr


