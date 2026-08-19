class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        bg = {}
        
        for i in reservedSeats:
            row,col = i
            if(row not in bg):
                bg[row] = []
            bg[row].append(col)
        
        count= (n-len(bg)) *2
        for row in bg:
            arr = [False] *10
            for i in bg[row]:
                arr[i-1] = True
            arr = arr[1:9]
            if(set(arr) == {False}):
                count +=2
            elif(arr[0:4] == [False]*4):
                count +=1
            elif(arr[2:6] == [False]*4):
                count +=1
            elif(arr[4:8] == [False]*4):
                count +=1
            
        return count
        
        
            
        
