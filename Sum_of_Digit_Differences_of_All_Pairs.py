class Solution:
    
    def sumDigitDifferences(self,nums):
        from collections import Counter

        
        str_nums = list(map(str, nums))
        n = len(str_nums)
        length = len(str_nums[0])
        total_diff = 0
    
       
        for i in range(length):
            digit_counts = Counter(num[i] for num in str_nums)
        
            
            for count in digit_counts.values():
                total_diff += count * (n - count)
    
        
        return total_diff // 2




