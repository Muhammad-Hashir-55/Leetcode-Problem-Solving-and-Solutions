class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        new_list = []
        for i in arr:
            if i not in new_list and arr.count(i) ==1:
                new_list.append(i)
        if (k > len(new_list)):
            return ""
        else:
            return new_list[k-1]
        

check = Solution()
print(check.kthDistinct(["hi","hello","hi"],1))