class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        def find_min(arr):
            n = len(arr)
            mini = inf
            for i in range(2,n):
                num = abs(arr[i-2] - arr[i-1]) + abs(arr[i-1] - arr[i]) + abs(arr[i] - arr[i-2])
                if(num < mini):
                    mini = num
            return mini


        dic = {}
        n = len(nums)
        ss = set()
        for i in range(n):
            if(nums[i] not in dic):
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(i)
            ss.add(nums[i])
        

        for i in ss:
            if(len(dic[i]) < 3):
                del dic[i]

        del ss
        if(not dic):
            return -1

        mini = inf
        for i in dic:
            arr = dic[i]
            num = find_min(arr)
            if(num < mini):
                mini = num
        return mini
