class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        mini1 = min(prices)
        prices.remove(mini1)
        mini2 = min(prices)
        if(money - (mini1 + mini2) >=0):
            return money - (mini1 + mini2)
        else:
            return money
