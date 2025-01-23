class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        arr =[]
        stack =[]
        prev =-99999
        for i in range(1,n+1):
            if(i in target):
                if(arr):
                    while(arr[-1]!=prev):
                        stack.append("Pop")
                        arr.pop()
                        if(not arr):
                            break

                arr.append(i)
                stack.append("Push")
                prev = i
            else:
                stack.append("Push")
                arr.append(i)
            if(arr ==target):
                break
        return stack


        
