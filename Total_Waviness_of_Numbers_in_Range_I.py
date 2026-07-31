class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        count = 0
        for i in range(num1,num2 +1):
            if(i<100):
                continue
            else:
                stri = str(i)
                n = len(stri)
                for j in range(1,n-1):
                    if(int(stri[j]) > int(stri[j-1]) and int(stri[j]) > int(stri[j+1])):
                        count +=1
                    elif(int(stri[j]) < int(stri[j-1]) and int(stri[j]) < int(stri[j+1])):
                        count +=1
        return count

        
