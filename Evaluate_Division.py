class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        gr = {}
        n = len(equations)
        for i in range(n):
            dr,dd = equations[i]
            v = values[i]
            if(dr not in gr):
                gr[dr] = {}
            if(dd not in gr):
                gr[dd] = {}
            gr[dr][dd] = v
            gr[dd][dr] = 1/v
    
        
        def dfs(node,dest,vis,gr,ans,temp):
            if(node in vis):
                return
            vis.add(node)
            if(node == dest):
                ans[0] = temp
                return
            
            for ne,val in gr[node].items():
                dfs(ne,dest,vis,gr,ans,temp*val)
        
        f_ans = []
        for i in queries:
            dr,dd = i
            if(dr not in gr or dd not in gr):
                f_ans.append(-1)
            else:
                temp = 1
                ans = [-1]
                vis = set()
                dfs(dr,dd,vis,gr,ans,temp)
                f_ans.append(ans[0])
        return f_ans

        

        
