class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        my_arr = []
        pos = set(positive_feedback)
        neg = set(negative_feedback)

        n = len(report)
        stds = student_id

        

        
        

        for i in range(n):
            tot = 0
            arr = report[i].split(' ')
            for j in arr:
                if(j in pos):
                    tot += 3
                elif(j in neg):
                    tot -=1
                else:
                    continue
            x = [stds[i] , tot]
            my_arr.append(x)
        my_arr.sort(key =lambda x : (-x[1] , x[0]))
        final = []
        
        for i in range(k):
            final.append(my_arr[i][0])
        return final


            

        
