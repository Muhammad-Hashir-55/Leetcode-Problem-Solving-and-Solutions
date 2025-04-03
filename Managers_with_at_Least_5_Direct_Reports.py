import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    x = list(employee.id)
    xx = list(employee.managerId)
    dic = {}
    for i in xx:
        if(i in dic):
            dic[i] +=1
        else:
            dic[i] = 1
    fin = []
    for i in dic:
        if(dic[i]>=5):
            fin.append(i)
    print(fin)
    df = employee[employee["id"].isin(fin)]["name"]
    df = pd.DataFrame({'name':df})
    return df

    
