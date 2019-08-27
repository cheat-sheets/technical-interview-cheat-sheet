import collections


def search(edges, start_node, method='dfs'):
    adj = collections.defaultdict(list)

    for f, t in edges:
        adj[f].append(t)

    visited = set()

    deq = collections.deque()

    deq.append(start_node)
    visited.add(start_node)

    while deq:
        if method == 'dfs':
            # stack for depth-first search
            node = deq.pop()
        elif method == 'bfs':
            # queue for breadth-first search
            node = deq.popleft()
        else:
            raise ValueError('Unknown method')

        print(node)

        children = adj[node]

        for child in children:
            if child not in visited:
                visited.add(child)
                deq.append(child)


search([("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E"), ("E", "A")], 'A', method='dfs')
