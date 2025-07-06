class Solution:
    def decodeString(self, s: str) -> str:
        alphas = []
        nums = []
        numbers= '0123456789'
        alpha = ''
        num = ''
        for i in s:
            if(i in numbers):
                num +=i
            elif(i == '['):
                nums.append(int(num))
                alphas.append(alpha)
                num = ''
                alpha = ''
            elif(i == ']'):
                last = alphas.pop()
                repeat = nums.pop()
                alpha = last + (alpha * repeat)
            else:
                alpha += i
        return alpha
