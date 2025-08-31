class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ss = set(friends)
        arr = []
        for i in order:
            if(i in ss):
                arr.append(i)
        return arr
        
