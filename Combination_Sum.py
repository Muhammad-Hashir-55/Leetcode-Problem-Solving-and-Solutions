class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def bt(idx,comb,tot):
            if(tot == target):
                res.append(comb[:])
                return
            if(idx >=len(candidates) or tot>target):
                return
            comb.append(candidates[idx])
            bt(idx,comb,tot+candidates[idx])
            comb.pop()
            bt(idx+1,comb,tot)

            return res
        return bt(0,[],0)
        
