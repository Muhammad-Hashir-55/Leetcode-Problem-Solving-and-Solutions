class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        mini = 0
        n = len(seats)
        for i in range(n):
            mini += abs(seats[i] - students[i])
        return mini
        
