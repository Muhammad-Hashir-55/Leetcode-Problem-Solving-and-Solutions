import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    dic= {}
    l1 = list(request_accepted.requester_id)
    for i in l1:
        if(i in dic):
            dic[i] +=1
        else:
            dic[i] = 1
    l2 = list(request_accepted.accepter_id)
    for i in l2:
        if(i in dic):
            dic[i] +=1
        else:
            dic[i] = 1
    maxi = -1
    idx = -1
    x1 = []
    x2 = []
    for i in dic:
        if(dic[i] > maxi):
            maxi = dic[i]
            idx = i
    x1.append(idx)
    x2.append(maxi)
    df = pd.DataFrame({'id':x1 , 'num': x2})
    return df
    
