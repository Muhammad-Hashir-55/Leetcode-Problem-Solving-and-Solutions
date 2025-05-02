import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    dic1 = {}
    dic2 = {}
    x1 = list(tree.id)
    x2 = list(tree.p_id)
    a1 = {}
    n = len(x1)
    for i in range(n):
        if(type(x2[i]) == pandas._libs.missing.NAType):
            a1[x1[i]]  = 'Root'
            x1.pop(i)
            x2.pop(i)
            break
    for i in x1:
        if(i in dic1):
            dic1[i] += 1
        else:
            dic1[i] =1
    for i in x2:
        if(i in dic2):
            dic2[i] +=1
        else:
            dic2[i] = 1
    for i in x1:
        if(i in dic2):
            a1[i] = 'Inner'
        else:
            a1[i]= 'Leaf'
    
    df = pd.DataFrame({'id': list(a1.keys()) , 'type':list(a1.values())})

    return df
        

    
