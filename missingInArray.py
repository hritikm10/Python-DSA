def missingNumber(self, arr):
    n = len(arr) + 1
    sum = 0
    for i in range(n - 1):
        sum += arr[i]
    expectedsum = n * (n + 1) // 2
    return expectedsum - sum


