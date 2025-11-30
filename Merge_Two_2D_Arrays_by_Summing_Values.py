class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dic = {}
        for i in nums1:
            if(i[0] in dic):
                dic[i[0]] += i[1]
            else:
                dic[i[0]] = i[1]

        for i in nums2:
            if(i[0] in dic):
                dic[i[0]] += i[1]
            else:
                dic[i[0]] = i[1]
        
        arr = []
        for i in dic:
            x = [i,dic[i]]
            arr.append(x)
        arr.sort()
        return arr

                

        
