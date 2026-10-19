import heapq

# THUẬT TOÁN DIJKSTRA (SHORTEST PATH ALGORITHM)
#
# 1. KHÁI NIỆM & NGUYÊN LÝ:
# - Dijkstra tìm đường đi ngắn nhất từ 1 đỉnh nguồn (single-source) tới mọi đỉnh khác
#   trên đồ thị có trọng số KHÔNG ÂM (Non-negative weights).
# - Áp dụng chiến lược Tham lam (Greedy Strategy): Luôn chọn đỉnh chưa thăm có khoảng cách nhỏ nhất hiện tại.
# - Nếu đồ thị có trọng số âm, Dijkstra không đảm bảo tính đúng đắn (khi đó cần dùng Bellman-Ford).

# 2. PHƯƠNG PHÁP 1: DÙNG MA TRẬN KỀ (ADJACENCY MATRIX) - O(V^2)
# Phù hợp với Đồ thị dày (Dense Graph, E ~ V^2)
INF = float('inf')

adj_matrix: list[list[float]] = [
    [0, 5, 3, INF, 11, INF],
    [5, 0, 1, INF, INF, 2],
    [3, 1, 0, 1, 5, INF],
    [INF, INF, 1, 0, 9, 3],
    [11, INF, 5, 9, 0, INF],
    [INF, 2, INF, 3, INF, 0],
]


def dijkstra_matrix(
    matrix: list[list[float]],
    start_node: int,
    target_node: int | None = None
) -> tuple[list[float], list[list[int]]]:
    """Tìm đường đi ngắn nhất bằng ma trận kề - O(V^2) thời gian, O(V^2) không gian."""
    n = len(matrix)
    distances = [INF] * n
    distances[start_node] = 0
    paths = [[node_no] for node_no in range(n)]
    visited = [False] * n

    for _ in range(n):
        min_distance = INF
        current = -1
        # Tìm đỉnh chưa thăm có khoảng cách nhỏ nhất: O(V)
        for node_no in range(n):
            if not visited[node_no] and distances[node_no] < min_distance:
                min_distance = distances[node_no]
                current = node_no

        if current == -1:
            break
        visited[current] = True

        # Cập nhật khoảng cách tới các đỉnh kề (Relaxation)
        for node_no in range(n):
            distance = matrix[current][node_no]
            if distance != INF and not visited[node_no]:
                new_distance = distances[current] + distance
                if new_distance < distances[node_no]:
                    distances[node_no] = new_distance
                    paths[node_no] = paths[current] + [node_no]

    targets = [target_node] if target_node is not None else range(n)
    for node_no in targets:
        if node_no == start_node or distances[node_no] == INF:
            continue
        # Dùng Generator Expression và str.join() để nối chuỗi đường đi ngắn gọn & tiết kiệm RAM:
        string_path = (str(n) for n in paths[node_no])
        path = ' -> '.join(string_path)
        print(f'{start_node} -> {node_no} | Distance: {distances[node_no]} | Path: {path}')

    return distances, paths


# 3. PHƯƠNG PHÁP 2: TỐI ƯU BẰNG MIN-HEAP (PRIORITY QUEUE) + DANH SÁCH KỀ - O((V + E) log V)
# Phù hợp với Đồ thị thưa (Sparse Graph, E << V^2)
# Graph dạng danh sách kề: {u: [(v, weight), ...]}
adj_list: dict[str, list[tuple[str, int]]] = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}


def dijkstra_heap(
    graph: dict[str, list[tuple[str, int]]],
    start: str,
    target: str | None = None
) -> tuple[dict[str, float], dict[str, list[str]]]:
    """Tìm đường đi ngắn nhất dùng Min-Heap (heapq) - O((V + E) log V) thời gian, O(V + E) không gian."""
    distances: dict[str, float] = {node: INF for node in graph}
    distances[start] = 0

    # Bảng tiền nhiệm (predecessor) để truy vết đường đi mà không cần lưu cả danh sách đường đi mỗi bước:
    previous: dict[str, str | None] = {node: None for node in graph}

    # Min-heap lưu tuple: (current_distance, node)
    pq: list[tuple[float, str]] = [(0, start)]

    while pq:
        curr_dist, u = heapq.heappop(pq)

        # Nếu lấy ra khoảng cách đã cũ (lớn hơn khoảng cách tối ưu hiện tại) -> bỏ qua:
        if curr_dist > distances[u]:
            continue

        # Nếu đã đến đích cần tìm -> có thể dừng sớm:
        if target is not None and u == target:
            break

        # Thao tác làm giãn (Edge Relaxation):
        for v, weight in graph[u]:
            new_dist = curr_dist + weight
            if new_dist < distances[v]:
                distances[v] = new_dist
                previous[v] = u
                heapq.heappush(pq, (new_dist, v))

    # Tái cấu trúc đường đi (Reconstruct Path) từ node đích ngược về node xuất phát:
    paths: dict[str, list[str]] = {}
    for node in graph:
        if distances[node] == INF:
            continue
        curr: str | None = node
        route: list[str] = []
        while curr is not None:
            route.append(curr)
            curr = previous[curr]
        route.reverse()
        paths[node] = route

    targets = [target] if target is not None else list(graph.keys())
    for node in targets:
        if node == start or distances[node] == INF:
            continue
        path_str = ' -> '.join(paths[node])
        print(f'{start} -> {node} | Distance: {distances[node]} | Path: {path_str}')

    return distances, paths


if __name__ == "__main__":
    print("--- 1. Dijkstra with Adjacency Matrix O(V^2) ---")
    dijkstra_matrix(adj_matrix, start_node=0, target_node=5)

    print("\n--- 2. Dijkstra with Min-Heap (heapq) O((V + E) log V) ---")
    dijkstra_heap(adj_list, start='A', target='F')
