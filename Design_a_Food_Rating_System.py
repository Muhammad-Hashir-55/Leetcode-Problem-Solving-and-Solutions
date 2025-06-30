from sortedcontainers import SortedList
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        n = len(foods)
        self.cui = {}
        self.foo = {}
        for i in range(n):
            if(cuisines[i] not in self.cui):
                self.cui[cuisines[i]] = SortedList()
                self.cui[cuisines[i]].add((-ratings[i] , foods[i]))
            else:
                self.cui[cuisines[i]].add((-ratings[i] , foods[i]))
            self.foo[foods[i]] = (cuisines[i] , ratings[i])
        
           
        

        

    def changeRating(self, food: str, newRating: int) -> None:
        cuis , rati = self.foo[food]
        self.foo[food] = (cuis , newRating)
        self.cui[cuis].discard((-rati , food))
        self.cui[cuis].add((-newRating , food))

        
        

    def highestRated(self, cuisine: str) -> str:
        return self.cui[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
