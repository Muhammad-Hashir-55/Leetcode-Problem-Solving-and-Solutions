class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count = 0
        digit = str(digit)
        for i in nums:
            x = str(i)
            num = x.count(digit)
            count += num
        return count

        
