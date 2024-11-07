class Solution:
    def frequencySort(self, nums):
        ans = []
        my_set = set(nums)
        n = len(my_set)
        count =1
        while(count<=len(nums)):
            c = False
            lis = []
            for i in my_set:

                if(nums.count(i)==count):
                    for j in range(nums.count(i)):
                        lis.append(i)
            lis.sort(reverse=True)
            for k in lis:
                ans.append(k)

            
            count +=1
        return ans
