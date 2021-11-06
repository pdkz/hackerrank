def icecreamParlor(m, arr):
    ht = {}
    for i, v in enumerate(arr):
        j = ht.get(m-v)
        if j != None and j >= 0:
            return sorted([i+1, j+1])
        ht[v] = i
