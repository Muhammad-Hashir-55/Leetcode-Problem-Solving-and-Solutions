class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        new_list = []
        text = text.split(" ")
        for i in range(len(text)-2):
            if(text[i]==first and text[i+1]==second):
                new_list.append(text[i+2])
        return new_list

        
