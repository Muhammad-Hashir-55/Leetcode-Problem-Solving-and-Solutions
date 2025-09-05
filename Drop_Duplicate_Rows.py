import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    dic = {'customer_id':[] , 'name':[] , 'email':[]}
    ss = set()
    for idx,row in customers.iterrows():
        if(row['email'] not in ss):
            dic['customer_id'].append(row['customer_id'])
            dic['name'].append(row['name'])
            dic['email'].append(row['email'])
            ss.add(row['email'])
    df = pd.DataFrame(dic)
    return df
    
