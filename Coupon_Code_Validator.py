class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        idxs = []
        n = len(code)
        for i in range(n):
            c = True
            if(not code[i]):
                idxs.append(i)
                continue
            for j in code[i]:
                if(j.upper() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'):
                    continue
                else:
                    c = False
                    break
            if(c ==False):
                idxs.append(i)
        for j in idxs[::-1]:
            code.pop(j)
            businessLine.pop(j)
            isActive.pop(j)
        
 
        
        idxs = []
        for i in range(len(code)):
            if(businessLine[i] not in ["electronics", "grocery", "pharmacy", "restaurant"]):
                idxs.append(i)

        for j in idxs[::-1]:
            code.pop(j)
            businessLine.pop(j)
            isActive.pop(j)
        

        
        idxs= []
        for j in range(len(isActive)):
            if(isActive[j] != True):
                idxs.append(j)
        
        for j in idxs[::-1]:
            code.pop(j)
            businessLine.pop(j)
            isActive.pop(j)
        

        
        n = len(code)
        for i in range(n):
            for j in range(i+1,n):
                if(businessLine[i]>businessLine[j]):
                    businessLine[i],businessLine[j] = businessLine[j],businessLine[i]
                    code[i],code[j] = code[j],code[i]
                elif(businessLine[i]==businessLine[j]):
                    if(code[i]>code[j]):
                        code[i],code[j] = code[j],code[i]

        return code



        



        
