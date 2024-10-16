class Solution:
    def generateTheString(self, n: int) -> str:
        if(n%2!=0):
            new_string = ""
            for i in range(n):
                new_string = new_string + 'a'
            return new_string
        else:
            new_string = ""
            for i in range(n-1):
                new_string = new_string + 'a'
            new_string = new_string +'b'
            return new_string

                
                



        
