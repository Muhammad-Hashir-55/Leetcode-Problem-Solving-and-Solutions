class Solution:
    def addSpaces(self, s: str, spaces) -> str:
        arr = []
        prev = 0
        for i in spaces:
            arr.append(s[prev:i])
            arr.append(" ")
            prev = i
        arr.append(s[prev:])
        s = ''
        for i in arr:
            s +=i
        return s
