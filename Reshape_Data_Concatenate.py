import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    std_ids = []
    names = []
    ages = []
    
    for index,row in df1.iterrows():
        std_ids.append(row['student_id'])
        names.append(row['name'])
        ages.append(row['age'])

    for index,row in df2.iterrows():
        std_ids.append(row['student_id'])
        names.append(row['name'])
        ages.append(row['age'])
    


    df = pd.DataFrame({'student_id':std_ids , 'name':names , 'age':ages})

    return df

    
