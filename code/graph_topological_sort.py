from collections import defaultdict


def topological_sort(edges):
    """Plucking off nodes with indegree 0 - also detects cycles"""
    adj = defaultdict(list)
    all_vertexes = set()
    indegrees = {}

    for f, t in edges:
        adj[f].append(t)

        all_vertexes.add(f)
        all_vertexes.add(t)

        indegrees[f] = indegrees.get(f, 0)
        indegrees[t] = indegrees.get(t, 0) + 1

    q = []
    for v, indeg in indegrees.items():
        if indeg == 0:
            q.append(v)

    result = []
    while q:
        v = q.pop()
        result.append(v)

        for v_tos in adj[v]:
            for v_to in v_tos:
                indegrees[v_to] -= 1
                if indegrees[v_to] == 0:
                    q.append(v_to)

    if len(result) != len(all_vertexes):
        return None
    return result


def flatten(list_of_lists):
    result = []
    for lst in list_of_lists:
        result.extend(lst)
    return result


edges = [('A', 'B'), ('B', 'D'), ('A', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F')]

res = topological_sort(edges)

print(res)


def topological_sort_via_dfs(edges):
    """Doesn't detect cycles (can be used only if we know there are no cycles)"""
    # reverse edges
    edges = [(t, f) for f, t in edges]
    all_vertices = set()

    adj = defaultdict(list)
    for f, t in edges:
        adj[f].append(t)
        all_vertices.add(f)
        all_vertices.add(t)

    not_visited = set(all_vertices)
    visited = set()

    sorted_v = []

    def dfs(v):
        if v in visited:
            return
        visited.add(v)
        not_visited.remove(v)
        children = adj.get(v)
        if children is not None:
            for child in children:
                dfs(child)

        sorted_v.append(v)

    while not_visited:
        any_v = not_visited.pop()
        not_visited.add(any_v)
        dfs(any_v)

    return sorted_v


edges = [('A', 'B'), ('B', 'D'), ('A', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F')]

res = topological_sort_via_dfs(edges)

print(res)
