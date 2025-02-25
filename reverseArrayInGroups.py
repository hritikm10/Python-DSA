def reverseInGroups(self, arr, k):
    n = len(arr)
    for i in range(0, n, k):
        left = i
        right = min(i + k - 1, n - 1)
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

# Iterates in steps of k to process each sub-array.
# Reverses elements in each sub-array using two pointers (left and right).
# Handles cases where the last group has fewer than k elements properly.
# Handles edge cases gracefully (e.g., k >= n, k = 1).