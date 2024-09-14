class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if(len(s)!= len(goal)):
            return False
        s= list(s)
        goal = list(goal)
        if(s == goal and len((set(s)))<len(goal)):
            return True
        different_indices= []
        for i in range(len(s)):
            if(s[i]!= goal[i]):
                different_indices.append(i)
        if(len(different_indices)==2):
            i,j = different_indices
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            return goal == s
        return False

        
