class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        index = -1
        if(ruleKey == "type"):
            index = 0
        elif(ruleKey == "color"):
            index = 1
        else:
            index = 2
        ans = 0
        for i in items:
            if(i[index]==ruleValue):
                ans +=1
        return ans

        
