class Bank:

    def __init__(self, balance: List[int]):
        self.arr = balance
        self.sett = set()
        idx = 0
        for i in self.arr:
            self.sett.add(idx)
            idx +=1
        
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if((account1 -1 ) in self.sett and (account2 -1 ) in self.sett and self.arr[account1 -1] >=money):
            self.arr[account2 - 1] += money
            self.arr[account1 - 1] -= money
            return True
        else:
            return False
        

    def deposit(self, account: int, money: int) -> bool:
        if(account - 1 in self.sett):
            self.arr[account - 1] += money   
            return True
        else:
            return False     

    def withdraw(self, account: int, money: int) -> bool:
        if(account - 1 in self.sett and self.arr[account - 1] >= money):
            self.arr[account - 1] -= money
            return True
        else:
            return False

        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
