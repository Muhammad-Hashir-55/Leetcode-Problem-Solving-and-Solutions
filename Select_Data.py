import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    dic = {'name':[], 'age':[]}
    for row,i in students.iterrows():
        if(i[0] == 101):
            dic['name'].append(i[1])
            dic['age'].append(i[2])
    df = pd.DataFrame(dic)
    return df

    
