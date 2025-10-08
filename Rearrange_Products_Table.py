import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    dic = {'product_id':[] , 'store': [], 'price': []}
    for idx,row in products.iterrows():
        if(pd.isnull(row['store1']) == False):
            dic['product_id'].append(row['product_id'])
            dic['store'].append('store1')
            dic['price'].append(row['store1'])
        if(pd.isnull(row['store2']) == False):
            dic['product_id'].append(row['product_id'])
            dic['store'].append('store2')
            dic['price'].append(row['store2'])
        if(pd.isnull(row['store3']) == False):
            dic['product_id'].append(row['product_id'])
            dic['store'].append('store3')
            dic['price'].append(row['store3'])
    df = pd.DataFrame(dic)
    return df
        
        
    
