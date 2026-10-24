class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        idx1 = arriveAlice.index('-')
        idx2 = leaveAlice.index('-')
        idx3 = arriveBob.index('-')
        idx4 = leaveBob.index('-')

        x1 = int(arriveAlice[:idx1])
        x2 = int(arriveAlice[idx1+1:])
        x3 = int(leaveAlice[:idx2])
        x4 = int(leaveAlice[idx2+1:])
        x5 = int(arriveBob[:idx3])
        x6 = int(arriveBob[idx3+1:])
        x7 = int(leaveBob[:idx4])
        x8 = int(leaveBob[idx4+1:])
    
        a = []
        while((x1,x2) != (x3,x4)):
            a.append(f"{x1:02d}-{x2:02d}")
            x2 +=1
            if(x1 == 2):
                if(x2 == 29):
                    x1 +=1
                    x2 = 1
            elif(x1 in [1,3,5,7,8,10,12]):
                if(x2 == 32):
                    x1 +=1
                    x2 = 1
            else:
                if(x2 == 31):
                    x1 +=1
                    x2 = 1
            
        a.append(f"{x3:02d}-{x4:02d}")
        ss = set(a)


        b = []
        while((x5,x6) != (x7,x8)):
            b.append(f"{x5:02d}-{x6:02d}")
            x6 += 1
            if(x5 == 2):
                if(x6 == 29):
                    x5 += 1
                    x6 = 1
            elif(x5 in [1,3,5,7,8,10,12]):
                if(x6 == 32):
                    x5 += 1
                    x6 = 1
            else:
                if(x6 == 31):
                    x5 += 1
                    x6 = 1
            
            
        b.append(f"{x7:02d}-{x8:02d}")
        
        count = 0
        for i in b:
            if(i in ss):
                count +=1
        return count

        
