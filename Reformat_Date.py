class Solution:
    def reformatDate(self, date: str) -> str:
        da = ""
        i=0
        while(date[i].isalpha()==False):
            da = da + date[i]
            i +=1
        day = int(da)

        s = date.split()
        month = 0
        if(s[1]=="Jan"):
            month =1
        elif(s[1]=="Feb"):
            month =2
        elif(s[1]=="Mar"):
            month =3
        elif(s[1]=="Apr"):
            month =4
        elif(s[1]=="May"):
            month =5
        elif(s[1]=="Jun"):
            month =6
        elif(s[1]=="Jul"):
            month =7
        elif(s[1]=="Aug"):
            month =8
        elif(s[1]=="Sep"):
            month =9
        elif(s[1]=="Oct"):
            month =10
        elif(s[1]=="Nov"):
            month =11
        elif(s[1]=="Dec"):
            month =12
        year = int(date[-4:])
        month = str(month)
        day = str(day)
        if(len(day)==1):
            day = "0"+day

        if(len(month)==1):
            month = "0"+month
        return str(year)+"-"+str(month)+"-"+str(day)
        

        
