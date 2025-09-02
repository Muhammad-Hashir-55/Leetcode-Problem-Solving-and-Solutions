from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        fin = []
        arr = SortedList()
        for i in range(k):
            arr.add(nums[i])
        elem = arr[x-1]
        if(elem >=0):
            fin.append(0)
        else:
            fin.append(elem)

        for i in range(k,n):
            arr.add(nums[i])
            arr.remove(nums[i-k]) #important
            
            if(len(arr) == k):
                elem = arr[x-1]
                if(elem >=0):
                    fin.append(0)
                else:
                    fin.append(elem)
        return fin

        
