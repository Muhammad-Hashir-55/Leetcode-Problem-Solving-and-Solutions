class ATM:

    def __init__(self):
        self.dic = {500:0,200:0,100:0,50:0,20:0}

        

    def deposit(self, banknotesCount: List[int]) -> None:
        x = banknotesCount
        self.dic[500] += x[-1]
        self.dic[200] += x[-2]
        self.dic[100] += x[-3]
        self.dic[50] += x[-4]
        self.dic[20] += x[-5]

        

    def withdraw(self, amount: int) -> List[int]:
        am = amount
        x = []
        dic = self.dic.copy()
        # important algorithm
        for note in [500, 200, 100, 50, 20]:
            count = min(am // note, dic[note])  # Max notes possible without exceeding amount
            am -= count * note
            x.append(count)
            dic[note] -= count

        if am != 0:
            return [-1]

        self.dic = dic
        return x[::-1]
        

            



        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
