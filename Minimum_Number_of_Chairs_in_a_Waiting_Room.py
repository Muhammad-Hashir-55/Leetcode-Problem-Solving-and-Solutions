class Solution:
    def minimumChairs(self, s: str) -> int:
        mini = 0
        arr = []
        for i in s:
            if(i == 'E'):
                mini +=1
            else:
                arr.append(mini)
                mini -=1
        arr.append(mini)
        x = max(arr)
        return x
        
