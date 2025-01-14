class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        n =len(time)
        c= 0
        freq = [0] * 60

        for i in time:
            rem = i%60
            if(rem == 0):
                c += freq[0]
            else:
                c += freq[60 - rem]
            freq[rem] +=1
        return c
            
                    
        
