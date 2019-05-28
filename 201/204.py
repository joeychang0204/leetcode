class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # will TLE now for new testcase
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
    def countPrimes(self, n: int) -> int:
        # eliminate prime's mutiples
        if n <= 2:
            return 0
        isPrime = [1] * n
        isPrime[0], isPrime[1] = 0, 0
        i = 2
        while i * i < n:
            if isPrime[i] == 1:
                j = i * 2
                while j < n:
                    isPrime[j] = 0
                    j += i
            i += 1
        return sum(isPrime)
