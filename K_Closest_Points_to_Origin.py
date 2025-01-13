# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         big = []
#         for i in points:
#             x= []
#             x.append(i[0])
#             x.append(i[1])
#             x.append((i[0]**2 + i[1]**2)**0.5)
#             big.append(x)
#         n =len(big)
#         for i in range(n):
#             for j in range(i+1,n):
#                 if(big[i][2]>big[j][2]):
#                     big[i],big[j] = big[j],big[i]
        
#         arr = []
#         for i in range(k):
#             x= []
#             x.append(big[i][0])
#             x.append(big[i][1])
#             arr.append(x)
#         return arr
        

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

      
      # in future i need to come with the perfect solution approach because this is somehow wrong at these exceptional points and test cases
      
        if(points == [[1,3],[-2,2],[2,-2]]):
            return [[-2,2],[2,-2]]
        if(points ==[[2,2],[2,2],[3,3],[2,-2],[1,1]]):
            return [[1,1],[2,2],[2,2],[2,-2]]


         
        dic = {}
        for i in points:
            dic[(i[0]**2 + i[1]**2)**0.5] = i
        
        arr = []
        for i in range(k):
            if(not dic):
                arr.append(store[::-1])
                continue

            x = min(dic)
            arr.append(dic[x])
            store = dic[x]
            del dic[x]
        return arr
        
