class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = bin(n)
        s = s[2:] 
        new_list =[]
        start = 0
        eve = 0
        for i in s:
            if(i =='1' and eve ==0):
                eve = 1
                start +=1
                continue
            if(i =='1' and eve ==1):
                new_list.append(start)
                start =0
                eve = 1
            if(eve ==1):
                start +=1
        if(not new_list):
            return 0
        else:
            return max(new_list)


        
