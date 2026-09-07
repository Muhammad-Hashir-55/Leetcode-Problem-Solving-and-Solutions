class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while(students):
            if(students[0] == sandwiches[0] ):
                students.pop(0)
                sandwiches.pop(0)
            else:
                if(len(set(students)) == 1 ):
                    break
                else:
                    x = students.pop(0)
                    students.append(x)
        return len(students)
                
        
