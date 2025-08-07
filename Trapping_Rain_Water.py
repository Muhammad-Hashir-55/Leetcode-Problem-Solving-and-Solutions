class Solution:
    def trap(self, height: List[int]) -> int:
        store = 0
        left = 0
        n = len(height)
        right = n -1
        l_maxi= 0
        r_maxi = 0
        while(left < right):
            if(height[left] < height[right]):
                if(l_maxi <= height[left]):
                    l_maxi = height[left]
                store += l_maxi - height[left]
                left +=1
            else:
                if(r_maxi <= height[right]):
                    r_maxi = height[right]
                store += r_maxi - height[right]
                right -=1
        return store
        
