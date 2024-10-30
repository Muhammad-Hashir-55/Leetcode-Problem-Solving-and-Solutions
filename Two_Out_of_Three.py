class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)
        big_list = []
        for i in set1:
            big_list.append(i)
        for j in set2:
            big_list.append(j)
        for k in set3:
            big_list.append(k)
        bs = set(big_list)
        ans = []
        for l in bs:
            if((l in set1 and l in set2) or (l in set1 and l in set3) or (l in set2 and l in set3)):
                ans.append(l)
        return ans

        
