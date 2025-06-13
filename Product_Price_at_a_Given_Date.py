import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    ids = list(products.product_id)
    dic = {}

    for i in ids:
        if(i not in dic):
            dic[i] = 10
    filtered = products[products['change_date'] <= '2019-08-16']
    filtered = filtered.sort_values(by=['product_id' , 'change_date'] , ascending=[True , False])



    visited = set()
    for index, row in filtered.iterrows():
        pid = row['product_id']
        if pid not in visited:
            dic[pid] = row['new_price']
            visited.add(pid)
    



    
    df = pd.DataFrame({'product_id':list(dic.keys()) , 'price':list(dic.values())})
    return df
    
    
    
