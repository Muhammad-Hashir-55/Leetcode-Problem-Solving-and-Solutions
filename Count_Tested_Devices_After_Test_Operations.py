class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        count = 0
        idx = 0
        c = False
        for i in batteryPercentages:
            if(i !=0):
                c = True
                break
            idx +=1
        if(not c):
            return 0
        
        x = 1
        
        for i in batteryPercentages[idx:]:
            if(i>=x):
                count +=1
                x +=1
        return count
        
