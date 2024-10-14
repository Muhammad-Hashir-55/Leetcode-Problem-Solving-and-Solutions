import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        date = datetime.datetime(year,month,day)
        day_of_week = date.strftime("%A")
        return day_of_week

