class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_dict = {}
        for i in nums:
            if(i not in my_dict):
                my_dict[i] =1
            else:
                my_dict[i] +=1
        maxi = -1
        for j in my_dict:
            if(my_dict[j]>maxi):
                maxi = my_dict[j]
        answer = 0
        for k in my_dict:
            if(my_dict[k]==maxi):
                answer += my_dict[k]
        return answer
