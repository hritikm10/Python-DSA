class Solution:
    def isPrime(self, n):
        prime = True
        if (n == 0 or n == 1):
            prime = False
        elif (n > 1):
            for i in range(2, n):
                if (n % i) == 0:
                    prime = False
                    break
        if prime:
            return True
        else:
            return False
