from Queue import PriorityQueue

n_rows, n_columns = [int(n) for n in raw_input().split()]
grid = [raw_input() for _ in range(n_rows)]
# coordinates are 1-indexed. Take 1 to make them 0-indexed:
car_row, car_col = [int(n) - 1 for n in raw_input().split()]

SYMBOLS = (WALL, CAR, DOOR) = ('#', 'c', 'D')

def adjacent_spaces(grid, row, column):
    """Yield the spaces adjacent to this one which are not blocked by walls"""
    n_rows, n_columns = len(grid), len(grid[0])
    for row_offset, col_offset in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        r, c = row + row_offset, column + col_offset
        if (r >= 0 and 
                r < n_rows and 
                c >= 0 and 
                c < n_columns and 
                grid[r][c] != WALL
                ):
            yield r, c

def is_edge(grid, row, column):
    n_rows, n_columns = len(grid), len(grid[0])
    return (row == 0 or column == 0 or 
            row == n_rows - 1 or column == n_columns - 1)

def is_exit(grid, row, column):
    return is_edge(grid, row, column) and grid[row][column] == DOOR

def cost(grid, row, column):
    return 1 if grid[row][column] == CAR else 0

def fewest_cars_to_move(grid, row, column):
    """Calculate the fewest number of cars you need to move to get a car from
    (row, column) to an exit of the grid."""
    n_rows, n_columns = len(grid), len(grid[0])
    costs = [[float("inf") for _ in range(n_columns)] for _ in
            range(n_rows)]
    costs[row][column] = 1 # 1 because there is a car here

    queue = PriorityQueue()
    queue.put((costs[row][column], (row, column)))

    while queue:
        current_row, current_col = queue.get()[1]
        if is_exit(grid, current_row, current_col):
            return costs[current_row][current_col]
        for next_row, next_col in adjacent_spaces(grid, current_row,
                current_col):
                alt_cost = costs[current_row][current_col] + cost(grid, next_row,
                        next_col)
                if alt_cost < costs[next_row][next_col]:
                    costs[next_row][next_col] = alt_cost
                    queue.put((alt_cost, (next_row, next_col)))

    raise Exception("Grid has no exit.")

print fewest_cars_to_move(grid, car_row, car_col)
