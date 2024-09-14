class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        list1 = []
        for i in s:
            if(i!="#"):
                list1.append(i)
            else:
                if(list1):
                    list1.pop()
        list2= []
        for j in t:
            if(j !="#"):
                list2.append(j)
            else:
                if(list2):
                    list2.pop()
        return list1 == list2


        
        

check = Solution()
print(check.backspaceCompare("ab#c","ad#c"))
