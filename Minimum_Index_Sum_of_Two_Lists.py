class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = []
        for i in list1:
            for j in list2:
                if(i == j):
                    common.append(i)
        indexes = []
        for i in common:
            idx1 = list1.index(i)
            idx2 = list2.index(i)
            indexes.append(idx1 + idx2)
        mini = min(indexes)
        final = []
        n = len(common)
        for i in range(n):
            if(indexes[i] == mini):
                final.append(common[i])
        return final



        
