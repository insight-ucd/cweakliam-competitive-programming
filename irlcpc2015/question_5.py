import functools
import math
import sys

memoize = functools.lru_cache(maxsize=None)
sys.setrecursionlimit(2500)


def dist(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


@memoize
def tour_length(v, c):
    last_visited_1 = locations[v]
    last_visited_2 = locations[c - 1]
    current = locations[c]
    
    if c == len(locations) - 1:
        return dist(last_visited_1, current) + dist(last_visited_2, current)

    return min(
            # make path between last_visited_1 and current
            tour_length(c - 1, c + 1) + dist(last_visited_1, current),
            # make path between last_visited_2 and current
            tour_length(v, c + 1) + dist(last_visited_2, current)
            )


def solve():
    return tour_length(0, 1)


n_locations = int(input())
locations = [
        tuple(int(x) for x in input().split())
        for _ in range(n_locations)
        ]

# sort by increasing x-coordinate
locations.sort(key=lambda point : point[0])

print("%.2f" % solve())
