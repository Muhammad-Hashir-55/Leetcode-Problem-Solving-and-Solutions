class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        ss = set()
        def get_primes_upto_1000():
            primes = []
            for num in range(2, 1001):
                is_prime = True
                for div in range(2, int(num ** 0.5) + 1):
                    if num % div == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(num)
            return primes
        primes = get_primes_upto_1000()
        for i in nums:
            x = i
            for j in primes:
                if(x ==1):
                    break

                while(x % j ==0):
                    x  = x //j
                    ss.add(j)
        print(ss)
        return len(ss)
