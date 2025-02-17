def largest(self, arr):
    n = len(arr)
    largest = -1
    for i in range(0, n):
        if (arr[i] > largest):
            largest = arr[i]
        else:
            continue
    return largest




