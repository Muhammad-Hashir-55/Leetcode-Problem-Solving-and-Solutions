class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        new_list = []
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if(words[i] in words[j]):
                    new_list.append(words[i])
                    continue
                elif(words[j] in words[i]):
                    new_list.append(words[j])
                    continue
        ans = []
        for j in new_list:
            if(j not in ans):
                ans.append(j)
        return ans


        
