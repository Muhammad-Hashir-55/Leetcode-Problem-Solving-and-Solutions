class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        n = len(s)
        i = 0
        nums = []
        while(i <n):
            a = ''
            if(s[i].isdigit()):
                while(i < n and s[i].isdigit()):
                    a += s[i]
                    i +=1
            if(a):
                nums.append(int(a))
                continue
            i +=1
        print(nums)
        k= sorted(nums)
        n = len(nums)
        if(n != len(set(nums))):
            return False
        if(nums == k):
            return True
        else:
            return False

        
