import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    departments = list(department['id'])
    real_names = list(department['name'])
    dic = dict(zip(departments, real_names))
    res = pd.DataFrame({'Department':[], 'Employee':[],'Salary':[]})
    for i in departments:
        x = []
        for row in employee.itertuples(index=True):
            if(i == row.departmentId):
                x.append(int(row.salary))
        x.sort(reverse=True)
        processed = set()
        print(x)
        
        for j in x:
            if(j not in processed):
                for row in employee.itertuples(index=True):
                    if(j == int(row.salary) and row.departmentId == i):
                        res.loc[len(res)] = [dic[i], row.name, row.salary]
            processed.add(j)
            if(len(processed) == 3):
                break
            
                
    return res



        
    
