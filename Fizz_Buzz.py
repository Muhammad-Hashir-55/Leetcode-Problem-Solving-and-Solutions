class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        new_list = []
        for i in range(1,n+1):
            if((i % 5 == 0) and (i %3 == 0)):
                new_list.append("FizzBuzz")
            elif(i == 3 or (i % 3 == 0)):
                new_list.append("Fizz")
            elif(i == 5 or(i % 5 == 0)):
                new_list.append("Buzz")
            else:
                new_list.append(str(i))
        return new_list
        