class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sumi_g = sum(gas)
        sumi_c = sum(cost)
        n = len(gas)
        if(sumi_g < sumi_c):
            return -1
        start = 0
        curr_g = 0
        for i in range(n):
            curr_g += gas[i] - cost[i]
            if(curr_g < 0):
                curr_g = 0
                start = i +1
        return start
        
