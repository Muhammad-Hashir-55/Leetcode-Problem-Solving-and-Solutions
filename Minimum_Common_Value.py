class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 =len(nums2)
        i =0
        j  =0
        while(i <n1 and j<n2):
            if(nums1[i]==nums2[j]):
                return nums1[i]
            elif(nums1[i]<nums2[j]):
                i +=1
            elif(nums1[i]>nums2[j]):
                j +=1
        return -1
        
