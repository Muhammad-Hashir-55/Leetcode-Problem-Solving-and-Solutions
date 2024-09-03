class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lm =1
        rm =1
        n=  len(nums)
        l_list = [0] *n
        r_list = [0] *n
        for i in range(n):
            j = -i-1
            l_list[i]= lm
            r_list[j] = rm
            lm *= nums[i]
            rm *= nums[j]
        answer = [0] * n

        for i in range(n):
            answer[i] = l_list[i] * r_list[i]
        return answer
            
        
