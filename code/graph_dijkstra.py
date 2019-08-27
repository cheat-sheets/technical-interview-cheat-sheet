import heapq
import collections


def dijkstra(edges, from_node, to_node):
    adj = collections.defaultdict(list)
    for f, t, distance in edges:
        adj[f].append((distance, t))

    heap = [(0, from_node, ())]
    min_distances = {}
    while heap:
        (distance, node, path) = heapq.heappop(heap)
        if node in min_distances:
            continue
        min_distances[node] = distance
        path = (node, path)
        if node == to_node:
            return distance, path

        for cost, dest_node in adj.get(node, ()):
            if dest_node not in min_distances:
                heapq.heappush(heap, (distance + cost, dest_node, path))

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
