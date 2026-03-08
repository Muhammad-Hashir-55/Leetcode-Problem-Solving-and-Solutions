class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ss = set()
        for i in emails:
            stri = i
            if('.' in stri):
                idx = stri.index('@')
                temp = stri[:idx]
                temp = stri.replace('.','')
                stri = temp + stri[idx:]
            if('+' in stri):
                idx = stri.index('@')
                temp = stri[idx:]
                stri = stri[:idx]
                final = ''
                found = False
                for j in stri:
                    if(j == '+'):
                        found  = True
                        continue
                    if(found == False):
                        final +=j
                    if(found == True):
                        if(j == '@'):
                            found = False
                            final +='@'
                        else:
                            continue
                stri = final
                stri += temp
            ss.add(stri)
        return len(ss)
        
