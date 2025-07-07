import random

class Solution:

    def __init__(self, nums: List[int]):
        self.ori = nums[:]
       

        

    def reset(self) -> List[int]:
        return self.ori
        

    def shuffle(self) -> List[int]:
        shuff = self.ori[:]
        random.shuffle(shuff)
        return shuff
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
