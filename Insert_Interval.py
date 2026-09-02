class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        idxs = []
        arr = []
        if(not intervals):
            return [newInterval]
        if(newInterval[1] <intervals[0][0]):
            intervals.insert(0,newInterval)
            return intervals
        for i in range(n):
            if(newInterval[0] <= intervals[i][1]):
                arr.append(min(newInterval[0], intervals[i][0]))
                arr.append(max(newInterval[1],intervals[i][1]))
                idxs.append(i)
                break
        if(newInterval[1] <intervals[i][1] and newInterval[1] < intervals[i][0] ):
            intervals.insert(i,newInterval)
            return intervals
                
        for x in range(i+1,n):
            if(newInterval[1] >= intervals[x][0]):
                idxs.append(x)
                arr[1] = max(newInterval[1],intervals[x][1])
        
        if(not idxs):
            intervals.append(newInterval)
            return intervals
        intervals[idxs[0]] = arr
        idxs.pop(0)
        for i in idxs[::-1]:
            intervals.pop(i)
        return intervals

        
