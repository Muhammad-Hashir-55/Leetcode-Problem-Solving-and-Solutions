class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        maxi = 0
        n = len(s)
        curr = ''
        for i in range(n):
            if(s[i] not in curr):
                curr +=s[i]
                maxi = max(maxi,len(curr))
            else:
                count = curr.count(s[i])
                if(count == 1):
                    curr += s[i]
                    maxi = max(maxi,len(curr))
                else:
                    curr += s[i]
                    curr = curr[1:]
                    check = True
                    while(check):
                        check = False
                        for j in curr:
                            if(curr.count(j) >2):
                                check = True
                                break
                        if(check):
                            curr = curr[1:]
                    maxi = max(maxi,len(curr))
        return maxi

                        
        
