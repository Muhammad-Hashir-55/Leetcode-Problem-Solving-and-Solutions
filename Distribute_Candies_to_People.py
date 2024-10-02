class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        i =0
        t =0
        new_list = [0] * num_people
        while(candies>0):
            t +=1
            if(candies<t):
                new_list[i% num_people] += candies
                break
            else:
                new_list[i% num_people] += t
                candies -=t
            i +=1
        return new_list
                
