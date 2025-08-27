class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        coun = 0
        for i in hours:
            if(i>= target):
                coun +=1
        return coun
        
