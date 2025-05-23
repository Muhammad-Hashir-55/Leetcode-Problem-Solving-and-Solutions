class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        dic1 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i',
 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q',
 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y',
 25: 'z'}
        dic2 = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8,
 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16,
 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
 'z': 25}
        
        


        arr = []
        for i in s:
            arr.append(i)
        
        sumi = 0
        
        for i in range(len(shifts)-1,-1,-1):
            x = shifts[i] + sumi
            sumi += shifts[i]
            x += dic2[arr[i]]
            x = x % 26
            
            
            arr[i] = dic1[x]
        s = ''
        for i in arr:
            s +=i
        return s



        
