class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        mini = 9999999
        for i in tasks:
            if((i[1] + i[0]) < mini):
                mini = i[0] + i[1] 
        return mini
