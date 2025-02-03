class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a = ''
        n1 = len(num1)
        n2 = len(num2)

        for i in range(n1):
            if(num1[i] == '+'):
                break
            else:
                a +=num1[i]
        b = ''
        for j in range(i+1,n1):
            if(num1[j] == 'i'):
                break
            else:
                b +=num1[j]
        c = ''
        for i in range(n2):
            if(num2[i] =='+'):
                break
            else:
                c +=num2[i]
        d= ''
        for j in range(i+1,n2):
            if(num2[j] =='i'):
                break
            else:
                d +=num2[j]
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        real = (a*c) - (b*d)
        imaginary = (a*d) + (b*c)
        return str(real) +'+' + str(imaginary)+'i'
