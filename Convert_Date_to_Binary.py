class Solution:
    def convertDateToBinary(self, date: str) -> str:
        arr = date.split('-')
        x = bin(int(arr[0]))[2:]
        y = bin(int(arr[1]))[2:]
        z = bin(int(arr[2]))[2:]
        return x + '-' + y + '-' + z
        
