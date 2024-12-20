class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = 'aeiou'
        c = 0
        for i in words[left:right+1]:
            if(i[0] in vowels and i[-1] in vowels):
                c +=1
        return c

        
