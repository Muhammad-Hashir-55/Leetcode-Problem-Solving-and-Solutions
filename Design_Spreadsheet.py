class Spreadsheet:

    def __init__(self, rows: int):
        self.dic = {}
        alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(rows):
            x_dic = {}
            for j in alphas:
                x_dic[j] = 0
            self.dic[i] = x_dic
        
        

    def setCell(self, cell: str, value: int) -> None:
        number = int(cell[1:])
        letter = cell[0]
        self.dic[int(number)-1][letter] = value
        

    def resetCell(self, cell: str) -> None:
        number = int(cell[1:])
        letter = cell[0]
        self.dic[int(number)-1][letter] = 0
        

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        x = formula.split('+')
        sumi = 0
        for i in x:
            if(i[0] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                sumi += int(i)
            else:
                number = i[1:]
                letter = i[0]
                sumi += self.dic[int(number)-1][letter]
        return sumi

        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
