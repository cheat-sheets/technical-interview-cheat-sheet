import collections


def search(edges, f, method='dfs'):
    adj = collections.defaultdict(list)

    for from_v, to_v in edges:
        adj[from_v].append(to_v)

    visited = set()

    deq = collections.deque()

    deq.append(f)

    while deq:
        if method == 'dfs':
            v = deq.pop()
        elif method == 'bfs':
            v = deq.popleft()
        else:
            raise ValueError('Unknown method')

        print(v)

        children = adj[v]

        for child in children:
            if child not in visited:
                visited.add(v)
                deq.append(child)


search([("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E"), ("E", "A")], 'A', method='dfs')
