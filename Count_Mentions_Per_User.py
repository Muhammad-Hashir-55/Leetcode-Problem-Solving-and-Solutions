class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        dic = {}
        for i in range(numberOfUsers):
            dic[i] = 0
        
        mentions = [0]* numberOfUsers
        events = sorted(events,key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))  #important
        print(events)
        
        for i in events:
            if(i[0] == 'MESSAGE'):
                k = i[2].split(' ')
                if(k == ['ALL']):
                    for j in range(len(mentions)):
                        mentions[j] +=1
                elif(k == ['HERE']):
                    for j in range(len(mentions)):
                        if(dic[j]<=int(i[1])):
                            mentions[j] +=1
                else:
                    for j in k:
                        x = int(j[2:])
                        mentions[x] +=1
                
                

            else:
                k = i[2].split(' ')
                for j in k:
                    dic[int(j)] = int(i[1]) + 60

        return mentions




        
