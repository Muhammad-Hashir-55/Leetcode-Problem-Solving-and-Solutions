# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        # q = [root]
        # arr = []
        # while(q):
        #     x = q.pop(0)
        #     if(x):
        #         arr.append(x.val)
        #     if(x.left):
        #         q.append(x.left)
        #     if(x.right):
        #         q.append(x.right)
        # print(arr)
        self.arr = []
        def ino(root):
            if(root == None):
                return
            ino(root.left)
            self.arr.append(root.val)
            ino(root.right)
        ino(root)
        self.idx = 0
        self.n = len(self.arr)


    def next(self) -> int:
        x = self.arr[self.idx]
        self.idx +=1
        return x
        

    def hasNext(self) -> bool:
        if(self.idx < self.n):
            return True
        else:
            return False
        
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
