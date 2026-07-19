import heapq


# ---------------- Dijkstra's Algorithm ---------------- #

def dijkstra(graph, source):
    """
    Dijkstra's Algorithm using Min-Heap

    Time Complexity : O((V + E) log V)
    Space Complexity: O(V)

    graph : Dictionary {u: [(v, weight), ...]}
    """

    n = len(graph)

    dist = [float('inf')] * n
    prev = [None] * n

    dist[source] = 0

    priority_queue = [(0, source)]
    visited = set()

    while priority_queue:

        current_dist, u = heapq.heappop(priority_queue)

        if u in visited:
            continue

        visited.add(u)

        for v, weight in graph[u]:

            if dist[u] + weight < dist[v]:

                dist[v] = dist[u] + weight
                prev[v] = u

                heapq.heappush(priority_queue, (dist[v], v))

    return dist, prev


# ---------------- Reconstruct Path ---------------- #

def reconstruct_path(prev, source, target):

    path = []

    node = target

    while node is not None:
        path.append(node)
        node = prev[node]

    path.reverse()

    if path and path[0] == source:
        return path

    return []


# ---------------- Graph Definition ---------------- #

graph = {

    0: [(1, 4), (2, 1)],

    1: [(3, 1)],

    2: [(1, 2), (3, 5)],

    3: [(4, 3)],

    4: [(5, 2)],

    5: []

}


# ---------------- Main Program ---------------- #

source = 0

dist, prev = dijkstra(graph, source)

print(f"\nShortest Paths from Vertex {source}\n")

print(f"{'Vertex':>8} {'Distance':>10} {'Path':>30}")

print("-" * 55)

for vertex in range(len(graph)):

    path = reconstruct_path(prev, source, vertex)

    if path:
        path_str = " -> ".join(map(str, path))
    else:
        path_str = "No Path"

    distance = dist[vertex] if dist[vertex] != float("inf") else "INF"

    print(f"{vertex:>8} {str(distance):>10} {path_str:>30}")