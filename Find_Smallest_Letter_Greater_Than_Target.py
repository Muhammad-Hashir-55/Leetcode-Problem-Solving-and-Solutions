class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        default = letters[0]
        letters.sort()
        check = False
        for i in letters:
            if(i>target):
                check = True
                return i
        if(check == False):
            return default


        
