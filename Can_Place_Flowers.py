class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if(n ==0):
            return True
        if(len(flowerbed) == 1):
            if(flowerbed[-1] == 1):
                return False
            else:
                return True

        if(flowerbed[0] == 0 and flowerbed[1] == 0):
            flowerbed[0] = 1
            n -=1
        if(n == 0):
            return True
        if(flowerbed[-1] == 0 and flowerbed[-2] == 0):
            flowerbed[-1] = 1
            n -=1
        if(n == 0):
            return True
        
        length = len(flowerbed)
    
        for i in range(1,length-1):
            if(flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -=1
            if(n == 0):
                return True
        if(n <=0):
            return True
        else:
            return False

        
