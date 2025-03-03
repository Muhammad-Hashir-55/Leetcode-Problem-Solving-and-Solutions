class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        arr = []
        t= nums.count(pivot)
        for i in range(t):
            arr.append(pivot)
        print(arr)
        a = []
        for i in nums:
            if(i <pivot):
                a.append(i)
        b = []
        
        for i in nums:
            if(i>pivot):
                b.append(i)
        fin = []
        for i in a:
            fin.append(i)
        for i in arr:
            fin.append(i)
        for i in b:
            fin.append(i)
        return fin
