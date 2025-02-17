def search(self, arr, x):
    n = len(arr)
    for i in range(0, n):
        if (arr[i] == x):
            return i
            break
        else:
            continue
    return -1
