class Solution:
    def nextGreaterElement(self, n: int) -> int:
        store = n
        s = str(n)
        k = sorted(s)
        nums = []
        for i in k:
            nums.append(i)
        print(nums)
        from itertools import permutations
        n = len(nums)
        arr = list(permutations(nums,n))
        arr.sort()

        for i in arr:
            s = ''
            for j in i:
                s +=j
            x = int(s)
            if(x>store):
                if(x > 2**31 -1):
                    return -1
                return x
        return -1

        
