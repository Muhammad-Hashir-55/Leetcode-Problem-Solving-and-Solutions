class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        seen = set()
        path = set()
        op = []
        g = {}
        for i in prerequisites:
            if(i[0] not in g):
                g[i[0]] = [i[1]]
            else:
                g[i[0]].append(i[1])
        


         
        def dfs(node):
            if(node in path):
                return True
            if(node in seen):
                return False

            seen.add(node)
            path.add(node)

        

            for i in g.get(node,[]):
                if(dfs(i)):
                    return True
            
            op.append(node)
            path.remove(node)

            return False

        for i in range(numCourses):
            if(dfs(i)):
                return []
        return op

        
