class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if(stack and stack[-1] == i):
                stack.pop()
            else:
                stack.append(i)
        new_string = ""
        for j in stack:
            new_string = new_string + j
        return new_string
