import heapq
import collections


def dijkstra(edges, v_from, v_to):
    adj = collections.defaultdict(list)
    for f, t, cost in edges:
        adj[f].append((cost, t))

    heap = [(0, v_from, ())]
    min_scores = {}
    while heap:
        (cost, v1, path) = heapq.heappop(heap)
        if v1 in min_scores: continue
        min_scores[v1] = cost
        path = (v1, path)
        if v1 == v_to: return cost, path

        for c, v2 in adj.get(v1, ()):
            if v2 not in min_scores:
                heapq.heappush(heap, (cost + c, v2, path))

    return float("inf")


edges = [
    ("A", "B", 1),
    ("A", "C", 2),
    ("B", "D", 5),
    ("C", "D", 2),
    ("A", "E", 0),
]

print("=== Dijkstra ===")
print(edges)
print("A -> D:", dijkstra(edges, "A", "D"))
