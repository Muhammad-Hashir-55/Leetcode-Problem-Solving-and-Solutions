class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j =n - 1
        maxi = max(nums)
        mini = min(nums)
        idx1 = nums.index(maxi)
        idx2 = nums.index(mini)
        arr = [idx1,idx2]
        arr.sort()
        a= []
        a.append(arr[-1] + 1)
        x = arr[0]
        x = x + (n - arr[1])
        x +=1
        a.append(x)

        x = (n - arr[0])
        
        a.append(x)

  
        return min(a)

        print(idx1,idx2)
        
