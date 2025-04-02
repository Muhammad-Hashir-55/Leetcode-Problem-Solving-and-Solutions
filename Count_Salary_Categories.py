import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    x = list(accounts.income)
    dic = {'Low Salary': 0 , 'Average Salary': 0 , 'High Salary': 0}
    for i in x:
        if(i < 20000):
            dic['Low Salary'] +=1
        elif(i>=20000 and i <= 50000):
            dic['Average Salary'] +=1
        else:
            dic['High Salary'] +=1
    df = pd.DataFrame({'category': dic.keys() , 'accounts_count':dic.values()})
    return df

    
