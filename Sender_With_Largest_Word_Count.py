class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        users= {}
        n = len(messages)
        for i in range(n):
            if(senders[i] not in users):
                a = messages[i].split(' ')
                users[senders[i]] = len(a)
            else:
                a = messages[i].split(' ')
                users[senders[i]] += len(a)
        aa = []
        for i in users:
            x = []
            x = [i,users[i]]
            aa.append(x)
        maxi = -1
        
        aaa = []
        for i in aa:
            if(maxi< i[1]):
                maxi = i[1]
        for i in aa[::-1]:
            if(i[1] == maxi):
                aaa.append(i[0])
        print(aaa)
        aaa.sort()
        return aaa[-1]
        


                

        
