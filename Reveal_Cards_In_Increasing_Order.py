class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        deck.sort()
        n = len(deck)
        idxs = list(range(n))
        arr = [0] *n
        for i in deck:
            idx = idxs.pop(0)
            arr[idx] = i
            if(idxs):
                x = idxs.pop(0)
                idxs.append(x)
        return arr
        
