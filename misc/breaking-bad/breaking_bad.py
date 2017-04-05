from collections import defaultdict
import sys
sys.setrecursionlimit(101000)


def read_input():
    n_items = int(raw_input())
    items = [raw_input() for _ in range(n_items)]
    n_pairs = int(raw_input())
    pairs = [raw_input().split() for _ in range(n_pairs)]

    graph = defaultdict(lambda : {'buyer': None, 'edges': []})
    for item1, item2 in pairs:
        graph[item1]['edges'].append(item2)
        graph[item2]['edges'].append(item1)

    return graph, items


def try_divide_subgraph(node, graph, buyer):
    next_buyer = 'jesse' if buyer == 'walter' else 'walter'

    if node['buyer'] == buyer:
        return True
    if node['buyer'] == next_buyer:
        return False

    # we haven't visited this node
    node['buyer'] = buyer
    return all(try_divide_subgraph(graph[edge], graph, next_buyer)
            for edge in node['edges'])


def try_divide_graph(graph):
    for node in graph.values():
        if not node['buyer']:
            if not try_divide_subgraph(node, graph, 'walter'):
                return False
    return True


def solve():
    graph, all_items = read_input()
    if not try_divide_graph(graph):
        print 'impossible'
        return

    walter_items = filter(
            lambda item: graph[item]['buyer'] == 'walter',
            graph.keys()
            )
    jesse_items = set(all_items) - set(walter_items)
    print ' '.join(walter_items)
    print ' '.join(jesse_items)


solve()
