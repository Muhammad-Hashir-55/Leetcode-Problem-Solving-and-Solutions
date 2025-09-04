class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(not digits):
            return []
        dic = {'2':['a','b','c'] ,'3':['d','e','f'] , '4':['g','h','i'],'5':['j','k','l'] , '6' : ['m','n','o'] , '7':['p','q','r','s'] , '8':['t','u','v'] , '9' : ['w','x','y','z'] }
        n= len(digits)
        res = []
        
        def backtrack(comb,digs):
            if(len(digs) == 0):
                res.append(comb)
                return
            curr = digs[0]
            letters = dic[curr]
            for i in letters:
                backtrack(comb + i, digs[1:])
        backtrack('',digits)
        return res
                
        
