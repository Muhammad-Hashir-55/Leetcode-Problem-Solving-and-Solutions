class Solution:
    def countBits(self, n: int) -> List[int]:
        new_list = [0]*(n+1)
        n = len(new_list)
        for i in range(0,n):
            new_string = bin(i)[2:]
            ones = 0
            for j in new_string:
                if(j == "1"):
                    ones +=1
            new_list[i] = ones
        return new_list
