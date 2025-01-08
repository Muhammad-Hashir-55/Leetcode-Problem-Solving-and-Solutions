class Solution:
    def countPrefixSuffixPairs(self, words) -> int:
        n = len(words)
        c =0
        for i in range(n):
            for j in range(i+1,n):
                if(len(words[i])==len(words[j]) and words[i]==words[j]):
                    c +=1
                    continue
                if(words[i] in words[j] and words[j].index(words[i])==0):
                    nn =len(words[j]) -1
                    while(nn>=0):
                        if(words[i]==words[j][-nn:]):
                            c +=1
                            break
                        nn -=1

        return c
