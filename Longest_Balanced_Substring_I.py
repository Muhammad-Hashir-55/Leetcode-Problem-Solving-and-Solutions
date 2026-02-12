class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            freq = [0]*26
            maxi = 0
            dis = 0
            for j in range(i,n):
                idx = ord(s[j]) - ord('a')
                if(freq[idx] == 0):
                    dis +=1
                freq[idx] +=1
                maxi = max(freq[idx],maxi)

                leng = j-i +1
                if(leng == dis * maxi):
                    ans = max(ans,leng)
        return ans
        
