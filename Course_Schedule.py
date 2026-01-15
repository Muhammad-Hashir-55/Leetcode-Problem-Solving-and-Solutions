class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course,pre in prerequisites:
            graph[course].append(pre)
        visited = set()
        path = set()
        def dfs(course):
            if(course in path):
                return False
            if(course in visited):
                return True
            
            path.add(course)

            for pre in graph[course]:
                if(not dfs(pre)):
                    return False
            path.remove(course)
            visited.add(course)
            return True # important step
        
        for course in range(numCourses):
            if(not dfs(course)):
                return False
        return True
