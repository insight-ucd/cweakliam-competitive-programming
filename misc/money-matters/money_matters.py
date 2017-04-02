n_friends, n_friendships = map(int, raw_input().split())
debts_list = [int(raw_input()) for _ in range(n_friends)]
friendships = [map(int, raw_input().split()) for _ in range(n_friendships)]

adjacency_lists = [[] for _ in range(n_friends)]
for friend1, friend2 in friendships:
    adjacency_lists[friend1].append(friend2)
    adjacency_lists[friend2].append(friend1)


def dfs(node, adjacency_lists, visited=set()):
    fringe = [node]
    while fringe:
        current = fringe.pop()
        # note that the contents of visited are preserved between calls
        # so this function can never visit the same node twice
        if current in visited:
            continue
        yield current
        visited.add(current)
        for next_node in adjacency_lists[current]:
            fringe.append(next_node)


def solvable(adjacency_lists, debts_list):
    for node, _ in enumerate(adjacency_lists):
        if sum(debts_list[friend] for friend in dfs(node, adjacency_lists)) != 0:
            return False
    return True


if solvable(adjacency_lists, debts_list):
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
