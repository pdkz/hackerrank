def connectedCell(matrix):
    depth = 0
    max_depth = 0
    
    max_x = len(matrix[0]) - 1
    max_y = len(matrix) - 1
    
    def dfs(matrix, y, x):
        nonlocal max_x
        nonlocal max_y
        nonlocal depth
        nonlocal max_depth
        if matrix[y][x] == 0:
            return

        depth += 1
        matrix[y][x] = 0
        
        dirs = [
            [y+1, x+1], [y+1, x], [y+1, x-1], 
            [y, x+1], [y, x-1],
            [y-1, x+1], [y-1, x], [y-1, x-1]
        ]

        for ny, nx in dirs:
            if nx < 0 or ny < 0 \
            or nx > max_x or ny > max_y \
            or matrix[ny][nx] == 0:
                max_depth = max(depth, max_depth)
                continue

            dfs(matrix, ny, nx)

    for y in range(max_y+1):
        for x in range(max_x+1):
            depth = 0
            dfs(matrix, y, x)
    return max_depth
