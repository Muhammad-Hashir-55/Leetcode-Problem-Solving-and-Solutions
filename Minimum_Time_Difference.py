class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        arr = timePoints
        print(arr)
        mini = 99999999
        n = len(arr)
        a = []
        for i in range(n):
    
            idx1 = arr[i].index(':')
      
            mins1 = int(arr[i][idx1 + 1:])
            hours1 = int(arr[i][:idx1])
            a.append(hours1 * 60 + mins1)
        
        print(a)
        a.sort()

        n = len(a)
        mini = 99999999
        for i in range(1,n):
            mini = min(mini , a[i] - a[i-1])
        
        return min(mini , 1440 + a[0] - a[-1])



        return mini
