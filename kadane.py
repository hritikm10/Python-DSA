def maxSubArraySum(self, arr):
    maximum = arr[0]
    recentmax = arr[0]
    for i in range(1, len(arr)):
        recentmax = max(recentmax + arr[i], arr[i])
        maximum = max(recentmax, maximum)
    return maximum

#Maximum Subarray Sum