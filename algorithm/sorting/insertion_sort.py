def insertionSort1(n, arr):
    for i in range(1, n):
        v = arr[i]
        j = i - 1
        while j >= 0 and v < arr[j]:
            arr[j+1] = arr[j]
            print(' '.join(map(str, arr)))
            j -= 1
        arr[j+1] = v
    print(' '.join(map(str, arr)))