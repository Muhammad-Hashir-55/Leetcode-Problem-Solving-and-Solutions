class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        new_dict = {}
        index  =0
        for i in heights:
            new_dict[i] = index
            index +=1
        new_list = list(sorted(new_dict.keys(),reverse=True))
        names_list = []
        for j in range(len(names)):
            names_list.append(names[new_dict[new_list[j]]])
        return names_list
        
