class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        n =len(score)
        for i in range(n):
            for j in range(i+1,n):
                if(score[i][k]<score[j][k]):
                    score[i],score[j] = score[j],score[i]
        return score
        
