class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        primes = [2]
        for i in range(3, n):
            isPrime = True
            for prime in primes:
                if prime * prime > i:
                    break
                if i % prime == 0:
                    isPrime = False
                    break
            if isPrime:
                primes.append(i)
        return len(primes)
