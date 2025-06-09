class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        arr = []
        m = len(mat)
        n = len(mat[0])
        final = m*n
        m -=1
        n -=1
        idx_m = 0
        idx_n = 0
        u_dir = True
        while(len(arr) != final):
            if(idx_m >m or idx_n > n):
                break
            arr.append(mat[idx_m][idx_n])
            if(u_dir == True):
                if(idx_m == 0 or idx_n == n):
                    if(idx_n < n):
                        idx_n +=1
                    else:
                        idx_m +=1
                    u_dir = False
                else:
                    idx_m -=1
                    idx_n +=1
            else:
                if(idx_n == 0 or idx_m == m):
                    if(idx_m < m):
                        idx_m +=1
                    else:
                        idx_n +=1
                    u_dir = True
                else:
                    idx_m +=1
                    idx_n -=1
        
        return arr

                
            




        
