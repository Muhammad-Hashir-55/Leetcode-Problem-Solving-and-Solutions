this is how i implemented

class Solution:

    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:

        graph = {}

        for u,v in invocations:

            if(u in graph):

                graph[u].append(v)

            else:

                graph[u] = [v]

        

        sus = set()

        sus.add(k)

        q = [k]

        while(q):

            u = q.pop(0)

            if(u not in graph):

                continue

            for v in graph[u]:

                if(v not in sus):

                    sus.add(v)

                    q.append(v)

        

        for u,v in invocations:

            if(u not in sus and v in sus):

                return list(range(n))

        

        ans = []

        for i in range(n):

            if(i not in sus):

                ans.append(i)

        return ans

        



this got accepted hehe
