class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_dict ={}
        for i in nums:
            if(i not in my_dict):
                my_dict[i] =1
            else:
                my_dict[i] +=1
        answer = 0
        maxi  =-1
        for j in my_dict:
            if(my_dict[j]>maxi):
                maxi = my_dict[j]
                answer = j
        return answer


        
