from collections import defaultdict
import sys
sys.setrecursionlimit(101000)


def read_input():
    """Read in the input and return a graph representing suspicious pairs of
    items, plus a list of all of the items (some of which may not be in the
    graph).
    
    The graph is a dict mapping an item name to a dict of {'buyer': None,
    'edges': [..]}, i.e. a slot for identifying who should buy the item, plus
    a list of 'edges', which are any items that are suspicious if bought with
    this one.
    """
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
    """Divide the items in the graph into items bought by Walter and items
    bought by Jesse. Mark the 'buyer' tag on each node with the name of the
    chosen buyer.

    Return False if the graph could not be divided without assigning
    a 'suspicious pair' to the same buyer. Return True otherwise.
    """
    for node in graph.values():
        # only check if the buyer tag has not been filled. If it has, then it
        # means we've already checked the whole sub-graph containing this node
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
