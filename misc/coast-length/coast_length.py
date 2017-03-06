square_types = (WATER, LAND) = (0, 1)


def adjacents(square, rows, cols):
    """given a square on a grid of size [rows, columns], yield the coordinates
    of the adjacent squares"""
    if square[0] - 1 >= 0:
        yield (square[0] - 1, square[1]) # up
    if square[0] + 1 < rows:
        yield (square[0] + 1, square[1]) # down
    if square[1] - 1 >= 0:
        yield (square[0], square[1] - 1) # left
    if square[1] + 1 < cols:
        yield (square[0], square[1] + 1) # right


def coast_DFS(grid):
    """use DFS to get the length of the coast for this grid.

    Assumes that the grid has a border of water all around it. This function
    uses DFS to find every square with sea water on it, while counting the
    number of kilometers of coast that each sea square creates.
    """
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    nodes = [(0,0)]
    coast_len = 0
    while nodes:
        curr = nodes.pop()
        if visited[curr[0]][curr[1]]:
            continue
        visited[curr[0]][curr[1]] = True

        for adj_square in adjacents(curr, rows, cols):
            i, j = adj_square
            if grid[i][j] == LAND:
                coast_len += 1
            else:
                nodes.append(adj_square)

    return coast_len


# read in the grid
rows, cols = (int(x) for x in raw_input().split())
grid = [[int(x) for x in list(raw_input())] for _ in range(rows)]

# add a border of water around it
grid.append([WATER for _ in range(cols)])
grid.insert(0, [WATER for _ in range(cols)])
for row in grid:
    row.append(WATER)
    row.insert(0, WATER)

print coast_DFS(grid)
