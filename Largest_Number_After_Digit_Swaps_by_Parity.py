class Solution:
    def largestInteger(self, num: int) -> int:
        arr = []
        s = str(num)
        for i in s:
            arr.append(int(i))
        n = len(arr)
        for i in range(n):
            for j in range(i+1,n):
                if(arr[i] %2 ==0 and arr[j]%2 ==0):
                    if(arr[i]<arr[j]):
                        arr[i],arr[j] = arr[j],arr[i]
                elif(arr[i]%2 != 0 and arr[j]%2 !=0):
                    if(arr[i]<arr[j]):
                        arr[i],arr[j] = arr[j],arr[i]
        print(arr)
        s = ''
        for i in arr:
            s += str(i)
        return int(s)
        
