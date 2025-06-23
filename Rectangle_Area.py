class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        tot = 0
        ax = ax2 - ax1
        ay = ay2 - ay1

        a = ax * ay
        tot += a

        

        bx = bx2 - bx1
        by = by2 - by1

        b = bx * by
        tot += b

        print(tot)

        comm_x1 = max(ax1 ,bx1)
        comm_y1 = max(ay1 , by1)
        comm_x2 = min(ax2 , bx2)
        comm_y2 = min(ay2 , by2)

        if(comm_x1 < comm_x2 and comm_y1 < comm_y2):
            comm_x = comm_x2 - comm_x1
            comm_y = comm_y2 - comm_y1

            common = comm_x * comm_y 
            tot -= common

        return tot


        
