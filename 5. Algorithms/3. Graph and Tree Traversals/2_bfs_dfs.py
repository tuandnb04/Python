from collections import deque

# Đồ thị / Cây mẫu dạng Adjacency List
graph: dict[str, list[str]] = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [], 'E': [], 'F': [], 'G': []
}

# Breadth-First Search (BFS) - Dùng Queue (FIFO)
# - Duyệt theo từng tầng (level-by-level)
# - Dùng tìm đường đi ngắn nhất (shortest path) trên đồ thị không trọng số
def bfs(start_node: str) -> list[str]:
    visited: list[str] = []
    queue: deque[str] = deque([start_node])
    seen: set[str] = {start_node}

    while queue:
        node = queue.popleft()        # Dequeue phần tử đầu hàng đợi
        visited.append(node)
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)# Enqueue vào cuối hàng đợi
    return visited

# Depth-First Search (DFS) - Dùng Đệ quy (hoặc Stack LIFO)
# - Chuẩn tối ưu: Dùng `seen` (set) để kiểm tra O(1), tránh bẫy O(V^2) khi dùng `in list`!
# - Độ phức tạp: O(V + E) thời gian, O(V) không gian
def dfs(node: str, visited: set[str] | None = None, order: list[str] | None = None) -> list[str]:
    if visited is None:
        visited = set()
    if order is None:
        order = []

    visited.add(node)
    order.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:    # O(1) Lookup
            dfs(neighbor, visited, order)
    return order

print("BFS (Queue):", " -> ".join(bfs('A'))) # A -> B -> C -> D -> E -> F -> G
print("DFS (Stack):", " -> ".join(dfs('A'))) # A -> B -> D -> E -> C -> F -> G

