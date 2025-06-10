class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            k = sorted(i)
            s = ''.join(k)
            if(s in dic):
                dic[s].append(i)
            else:
                dic[s] = []
                dic[s].append(i)
        final = []
        for i in dic:
            x = []
            for j in dic[i]:
                x.append(j)
            final.append(x)
        return final

        
