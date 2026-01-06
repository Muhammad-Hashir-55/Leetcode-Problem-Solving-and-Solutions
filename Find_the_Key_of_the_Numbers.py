class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        s1 = str(num1)
        s2 = str(num2)
        s3 = str(num3)
        arr = [s1,s2,s3]

        for i in range(3):
            while(len(arr[i]) != 4):
                arr[i] = '0' + arr[i]
        s = ''
        for i in range(4):
            mini = min([arr[0][i], arr[1][i], arr[2][i]])
            s += mini
        return int(s)
        
