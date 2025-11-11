class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        ss = set()
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i in words:
            l = ''
            for j in i:
                l += codes[ord(j) -97]
            ss.add(l)
        return len(ss)

        

        
