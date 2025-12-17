class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:

        nn = n        
        arr = []
        n = len(s)
        for i in range(n):
            x = 0
            curr = startPos[:]
            for j in range(i,n):
                if(s[j] == 'L'):
                    curr[1] -=1
                    if(curr[1]<0):
                        break
                elif(s[j] == 'R'):
                    curr[1] +=1
                    if(curr[1] == nn):
                        break
                elif(s[j] == 'U'):
                    curr[0] -=1
                    if(curr[0]<0):
                        break
                elif(s[j] == 'D'):
                    curr[0] +=1
                    if(curr[0] == nn):
                        break
                x +=1
            arr.append(x)
        return arr
                    

        
