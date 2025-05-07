class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invlds= []
        for i,tran in enumerate(transactions):
            n1 , t1, a1 , c1 = tran.split(',')
            if(int(a1) > 1000):
                invlds.append(tran)
                continue
            for j , tr in enumerate(transactions):
                n2,t2,a2,c2 = tr.split(',')
                if(i != j):
                    if(n1 == n2 and c1 != c2 and abs(int(t1) - int(t2)) <= 60):
                        invlds.append(tran)
                        break
        return invlds
        
