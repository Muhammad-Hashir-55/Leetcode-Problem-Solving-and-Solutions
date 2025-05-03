import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    df = queue.sort_values(by='turn')
    sumi = 0
    
    x = list(df.weight)
    id = 0
    for i in x:
        sumi += i
        if(sumi >1000):
            break
        id +=1
    turn = id
    name = queue.loc[queue['turn'] == turn, 'person_name'].values[0]

    df = ''
    dic = {'person_name':[name]}
    df = pd.DataFrame(dic)
    return df



    
