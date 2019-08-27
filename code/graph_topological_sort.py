from collections import defaultdict


def topological_sort(edges):
    """Plucking off nodes with indegree 0 - also detects cycles"""
    adj = defaultdict(list)
    all_nodes = set()
    indegrees = {}

    for f, t in edges:
        adj[f].append(t)

        all_nodes.add(f)
        all_nodes.add(t)

        indegrees[f] = indegrees.get(f, 0)
        indegrees[t] = indegrees.get(t, 0) + 1

    stack = []
    for node, indegree in indegrees.items():
        if indegree == 0:
            stack.append(node)

    result = []
    while stack:
        node = stack.pop()
        result.append(node)

        for child in adj[node]:
            indegrees[child] -= 1
            if indegrees[child] == 0:
                stack.append(child)

    if len(result) != len(all_nodes):
        return None
    return result


edges = [('A', 'B'), ('B', 'D'), ('A', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F')]

res = topological_sort(edges)

print('Topological sort by plucking off nodes:')
print(res)


def topological_sort_via_dfs(edges):
    """Doesn't detect cycles (can be used only if we know there are no cycles)"""
    # reverse edges
    edges = [(t, f) for f, t in edges]
    all_nodes = set()

    adj = defaultdict(list)
    for f, t in edges:
        adj[f].append(t)
        all_nodes.add(f)
        all_nodes.add(t)

    not_visited = set(all_nodes)
    visited = set()

    sorted_nodes = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        not_visited.remove(node)
        children = adj.get(node)
        if children is not None:
            for child in children:
                dfs(child)

        sorted_nodes.append(node)

    while not_visited:
        any_node = not_visited.pop()
        not_visited.add(any_node)
        dfs(any_node)

    return sorted_nodes


edges = [('A', 'B'), ('B', 'D'), ('A', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F')]

res = topological_sort_via_dfs(edges)

print('Topological sort by depth-first search:')
print(res)
