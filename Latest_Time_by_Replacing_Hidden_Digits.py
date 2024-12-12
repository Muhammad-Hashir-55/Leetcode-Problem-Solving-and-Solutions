class Solution:
    def maximumTime(self, time: str) -> str:
        if('?' not in time):
            return time
        n = len(time)
        if(time[0]=='?'):
            # time = time.replace('?','2',1)
            if(time[1]=='?'):
                time = time.replace('?','2',1)
                
            elif(int(time[1])>3):
                time= time.replace('?','1',1)
            else:
                time = time.replace('?','2',1)

        if(time[1]=='?'):
            # time = time.replace('?','3',1)
            if(int(time[0])==1 or int(time[0])==0):
                time = time.replace('?','9',1)
            else:
                time = time.replace('?','3',1)
        if(time[3] =='?'):
            time = time.replace('?','5',1)

        if(time[4]=='?'):
            time = time.replace('?','9',1)
        return time
