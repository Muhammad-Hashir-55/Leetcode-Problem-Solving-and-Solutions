class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ss = "0abcdefghijklmnopqrstuvwxyz"
        new_string = ""
        for i in s:
            new_string = new_string + str(ss.index(i))
        i = 0
        sum = 0
        while(i<k):
            sum =0
            for j in new_string:
                sum = sum + int(j)
            new_string = str(sum)
            i+=1
        return sum


check = Solution()
print(check.getLucky("leetcode",2))
