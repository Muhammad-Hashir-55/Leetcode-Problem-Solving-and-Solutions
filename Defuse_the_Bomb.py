class Solution:
    def decrypt(self, code, k: int):
        n = len(code)
        arr = []
        if(k ==0):
            return [0]*n
        print("done")
        if(k>0):
            for i in range(n):
                ii = i +1
                sumi =0
                for j in range(k):
                    sumi = sumi + code[(ii)%n]
                    ii +=1
                arr.append(sumi)
            return arr
        if(k<0):
            for i in range(n):
                ii = i -1
                sumi =0
                for j in range(abs(k)):
                    sumi = sumi + code[ii]
                    ii -=1
                
                arr.append(sumi)
                print(arr)
            return arr
