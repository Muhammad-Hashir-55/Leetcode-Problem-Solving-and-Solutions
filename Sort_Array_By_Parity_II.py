class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l1 =[]
        for i in nums:
            if(i % 2 ==0):
                l1.append(i)
        l2 =[]
        for j in nums:
            if(j % 2 != 0):
                l2.append(j)
        k =0
        l= 0
        ans = []
        while(k<len(l1) or l<len(l2)):
            if(k<len(l1)):
                ans.append(l1[k])
            if(l<len(l2)):
                ans.append(l2[l])
            k +=1
            l +=1
        return ans
    
check = Solution()
print(check.sortArrayByParityII([2,3]))
