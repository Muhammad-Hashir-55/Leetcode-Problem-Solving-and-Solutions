class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        bg = []
        for i in image:
            x = i[::-1]
            a = []
            for j in x:
                if(j == 0):
                    a.append(1)
                else:
                    a.append(0)
            bg.append(a)
        return bg
        
