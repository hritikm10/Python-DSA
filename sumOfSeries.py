def sumOfSeries(self, n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 3
    return sum