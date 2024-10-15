import datetime

class Solution:
    def dayOfYear(self, date: str) -> int:
        year = int(date[:4])
        month = int(date[5:7])
        days = int(date[8:])
        if((year %4 == 0 and year %100!=0)or (year %400 ==0)):
            total_days = 366
            if(month ==1):
                return days
            elif(month == 2):
                return 31 + days
            elif(month == 3):
                return 31 + 29+days
            elif(month ==4):
                return 31 + 29+31+days
            elif(month ==5):
                return 31 + 29 + 31+30+days
            elif(month ==6):
                return 31+29+31+30+31+ days
            elif(month ==7):
                return 31+29+31+30+31+30+days
            elif(month ==8):
                return 31+29+31+30+31+30+31+days
            elif(month ==9):
                return 31+29+31+30+31+30+31+31+days
            elif(month ==10):
                return 31+29+31+30+31+30+31+31+30+days
            elif(month ==11):
                return 31+29+31+30+31+30+31+31+30+31+days
            elif(month ==12):
                return 31+29+31+30+31+30+31+31+30+31+30+days
        else:
            if(month ==1):
                return days
            elif(month == 2):
                return 31 + days
            elif(month == 3):
                return 31 + 28+days
            elif(month ==4):
                return 31 + 28+31+days
            elif(month ==5):
                return 31 + 28 + 31+30+days
            elif(month ==6):
                return 31+28+31+30+31+ days
            elif(month ==7):
                return 31+28+31+30+31+30+days
            elif(month ==8):
                return 31+28+31+30+31+30+31+days
            elif(month ==9):
                return 31+28+31+30+31+30+31+31+days
            elif(month ==10):
                return 31+28+31+30+31+30+31+31+30+days
            elif(month ==11):
                return 31+28+31+30+31+30+31+31+30+31+days
            elif(month ==12):
                return 31+28+31+30+31+30+31+31+30+31+30+days
