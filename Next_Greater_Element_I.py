class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        checking = False
        ans = []
        for i in nums1:
            if(nums2.index(i)==len(nums2)-1):
                ans.append(-1)
            else:
                n1 = nums2.index(i)
                m1 = nums2[n1]
                m2 = nums2[n1+1]
                if(m2> m1):
                    ans.append(m2)
                    continue
                checking = False
                for j in nums2[n1:]:
                    if(j>m1):
                        m2 = j
                        ans.append(m2)
                        checking  = True
                        break
                if(checking == True):
                    continue
                
                if(m1>=m2):
                    ans.append(-1)
        return ans

        
