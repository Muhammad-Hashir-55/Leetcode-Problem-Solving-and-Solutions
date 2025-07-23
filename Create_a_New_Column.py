import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    name = list(employees['name'])
    salary = list(employees['salary'])
    bonus = []
    for i in salary:
        bonus.append(i*2)
    
    df = pd.DataFrame({'name':name , 'salary':salary , 'bonus':bonus})
    return df
    
