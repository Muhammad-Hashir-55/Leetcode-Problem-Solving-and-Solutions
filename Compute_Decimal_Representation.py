class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        s = str(n)
        nums = []
        num = s[0]
        n = len(s)
        for i in range(1,n):
            if(s[i] == '0'):
                num += s[i]
            else:
                size = n- i
                nums.append(num +  ('0' * size))
                num = s[i]
        size = 0
        nums.append(num + ('0' * size))
        
        arr = []
        for i in nums:
            arr.append(int(i))
        return arr
            
        
