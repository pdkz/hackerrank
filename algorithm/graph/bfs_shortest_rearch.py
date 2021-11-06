from collections import deque

def bfs(n, m, edges, s):
    s -= 1
    g = []
    for i in range(n):
        g.append([])

    for e in edges:
        i, j = e
        g[i-1].append(j-1)
        g[j-1].append(i-1)

    distances = [-1 for i in range(n)]
    visited = {s}

    queue = deque([(s, 0)])
    while len(queue) > 0:
        node, dist = queue.popleft()

        dist += 6
        for next_node in g[node]:
            if next_node in visited:
                continue
            visited.add(next_node)
            distances[next_node] = dist
            queue.append((next_node, dist))

    del distances[s]
    return distances
