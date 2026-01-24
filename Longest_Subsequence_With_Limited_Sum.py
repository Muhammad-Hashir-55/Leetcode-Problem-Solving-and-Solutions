class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        arr = []
        nums.sort()
        for i in queries:
            num = -inf
            size = 0
            sumi = 0
            for j in nums:
                sumi +=j
                if(sumi > i):
                    break
                size +=1
            arr.append(size)
        return arr



        
