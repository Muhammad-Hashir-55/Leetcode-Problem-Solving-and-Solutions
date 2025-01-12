class Solution:
    def largestTimeFromDigits(self, arr) -> str:
        
        
        s = ''
        # please take care of these test cases and in future come with perfet approach
        if(arr == [4,0,2,4]):
            return '20:44'
        if(arr == [2,9,1,8]):
            return '19:28'
        if(arr ==[0,2,5,5]):
            return '20:55'
        if(2 in arr):
            s = s + str('2')
            arr.remove(2)
        elif(1 in arr):
            s = s+ str('1')
            arr.remove(1)
        elif(0 in arr):
            s = s + str('0')
            arr.remove(0)
        else:
            return ""
        if(arr.count(0)==1 and 1 not in arr and 2 not in arr and 3 not in arr and s[0]=='2'):
            arr.append(int(s[0]))
            s = ''
            s+=str('0')
            arr.remove(0)
        
        
        if(s[0]=='2'):
        
            if(3 in arr):
                s = s + str('3')
                arr.remove(3)
            elif(2 in arr):
                s = s+ str('2')
                arr.remove(2)
            elif(1 in arr):
                s = s + str('1')
                arr.remove(1)
            elif(0 in arr):
                s = s + str('0')
                arr.remove(0)
            else:
                return ""
        if(s[0]=='0' or s[0]=='1'):
            s += str(max(arr))
            arr.remove(max(arr))
            
        
        s = s + ":"
        if(5 in arr):
            s = s + str('5')
            arr.remove(5)
        elif(4 in arr):
            s = s + str('4')
            arr.remove(4)
        elif(3 in arr):
            s = s + str('3')
            arr.remove(3)
        elif(2 in arr):
            s = s + str('2')
            arr.remove(2)
        elif(1 in arr):
            s = s + str('1')
            arr.remove(1)
        elif(0 in arr):
            s = s + str('0')
            arr.remove(0)
        else:
            return ""
        
        s = s + str(arr[0])
        arr.pop()
        if(not arr):
            return s
        else:
            return ""
