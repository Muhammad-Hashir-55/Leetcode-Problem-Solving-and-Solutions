class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        a = []
        for i in range(lo,hi+1):
            a.append(i)

        dic = {}
        for i in a:
            st =0
            x = i
            while(x != 1):
                if(x % 2 == 0):
                    x = x //2
                else:
                    x = 3 * x +1
                st +=1
            dic[i] = st
        
        


        for i in range(len(a)):
            for j in range(i+1,len(a)):
                if(dic[a[i]]> dic[a[j]]):
                    a[i],a[j] = a[j],a[i]
                elif(dic[a[i]] == dic[a[j]]):
                    if(a[i]>a[j]):
                        a[i], a[j] = a[j] , a[i]
        return a[k -1]
                    



                
        
