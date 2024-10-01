class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_ones(x):
            return bin(x).count('1')
        def sorting_key(x):
            return (count_ones(x),x)
        sorted_arr = sorted(arr,key = sorting_key)
        return sorted_arr
        
