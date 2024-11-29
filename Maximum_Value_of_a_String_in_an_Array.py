class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = []
        for i in strs:
            if(i.isdigit()):
                ans.append(int(i))
            else:
                ans.append(len(i))
        return max(ans)

        
