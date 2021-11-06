def rotateLeft(d, arr):
    # Write your code here
    for i in range(d):
        popd = arr.pop(0)
        arr.append(popd)
    return arr
