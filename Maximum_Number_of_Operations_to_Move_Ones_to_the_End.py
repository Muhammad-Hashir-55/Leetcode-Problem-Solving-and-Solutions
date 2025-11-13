class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        ones = 0
        n = len(s)

        for i, ch in enumerate(s):
            if ch == '1':
                ones += 1
            else:  # ch == '0'
                # if this zero is the last char or next char is '1',
                # it's a boundary that allows all previous '1's to be moved (one each)
                if i + 1 == n or s[i + 1] == '1':
                    ans += ones

        return ans
