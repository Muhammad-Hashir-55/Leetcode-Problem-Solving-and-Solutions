class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        pos = 0
        for i in commands:
            if(i == 'RIGHT'):
                pos +=1
            elif(i == 'LEFT'):
                pos -=1
            elif(i == 'DOWN'):
                pos +=n
            else:
                pos -=n
        return pos
        
