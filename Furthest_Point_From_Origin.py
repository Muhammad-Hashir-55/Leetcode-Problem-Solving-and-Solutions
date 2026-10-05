class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        cl = moves.count('L')
        cr = moves.count('R')

        if(cl >= cr):
            moves = moves.replace('_','L')
            return moves.count('L') - moves.count('R')
        else:
            moves = moves.replace('_','R')
            return moves.count('R') - moves.count('L')
        
