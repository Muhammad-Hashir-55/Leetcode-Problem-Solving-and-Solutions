class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        floor = 0
        count = 0
        for i in requests:
            x = abs(i-floor)
            count +=x
            floor = i
        return count
        
