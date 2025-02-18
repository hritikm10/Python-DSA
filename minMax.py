def get_min_max(self, arr):
    arr.sort()
    n = len(arr)
    minimum = 0
    max = 0
    if (len(arr) == 1):
        minimum = arr[0]
        maximum = arr[0]
    else:
        minimum = arr[0]
        maximum = arr[-1]

    return minimum, maximum