import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        year1 = int(date1[:4])
        month1= int(date1[5:7])
        days1 = int(date1[8:])
        s = datetime.datetime(year1,month1,days1)
        year2 = int(date2[:4])
        month2= int(date2[5:7])
        days2 = int(date2[8:])
        t = datetime.datetime(year2,month2,days2)
        diff = abs(s-t)
        return diff.days

        
