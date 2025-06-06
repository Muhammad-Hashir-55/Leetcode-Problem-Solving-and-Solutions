class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        arr = favoriteCompanies
        final  = []
        n = len(arr)
        for i in range(n):
            c = True
            for j in range(n):
                if(i == j):
                    continue
                if(set(arr[i]).issubset(arr[j])):
                    c = False
                    break
            if(c == True):
                final.append(i)
        return final

            




        
