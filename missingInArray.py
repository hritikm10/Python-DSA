def missingNumber(self, arr):
    n = len(arr) + 1
    sum = 0
    for i in range(n - 1):
        sum += arr[i]
    expectedsum = n * (n + 1) // 2
    return expectedsum - sum

#The sum of the first n natural numbers is given by the formula (n * (n + 1)) / 2. The idea is to compute this sum and subtract the sum of all elements in the array from it to get the missing number.
