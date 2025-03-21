import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    x1 = []
    for i in student_data:
        x1.append(i[0])
    x2 = []
    for i in student_data:
        x2.append(i[1])
    
    df = pd.DataFrame({'student_id':x1,
        'age':x2
    })
    return df    
