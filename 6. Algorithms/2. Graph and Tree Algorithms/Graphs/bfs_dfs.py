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
        node = queue.popleft()  # Dequeue phần tử đầu hàng đợi
        visited.append(node)
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)  # Enqueue vào cuối hàng đợi
    return visited


# 2. Depth-First Search (DFS) - Dùng Đệ quy (Recursive Call Stack)
# - Dùng set để kiểm tra visited trong O(1)
# - Độ phức tạp: O(V + E) thời gian, O(V) không gian
def dfs(node: str, visited: set[str] | None = None, order: list[str] | None = None) -> list[str]:
    if visited is None:
        visited = set()
    if order is None:
        order = []

    visited.add(node)
    order.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:  # O(1) Lookup
            dfs(neighbor, visited, order)
    return order


# 3. Iterative DFS trên Adjacency List (Dùng Stack LIFO tường minh)
# - Khử đệ quy để tránh lỗi RecursionError khi đồ thị có độ sâu lớn
# - Độ phức tạp: O(V + E) thời gian, O(V) không gian
def dfs_iterative(start_node: str) -> list[str]:
    visited: list[str] = []
    seen: set[str] = {start_node}
    stack: list[str] = [start_node]

    while stack:
        node = stack.pop()
        visited.append(node)
        # Duyệt ngược để đỉnh đầu tiên trong danh sách kề nằm trên đỉnh stack và được duyệt trước
        for neighbor in reversed(graph[node]):
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    return visited


# 4. Iterative DFS trên Adjacency Matrix (Ma trận kề)
# - Độ phức tạp: O(V^2) thời gian (do mỗi đỉnh phải duyệt qua toàn bộ V cột), O(V) không gian
# - Dùng visited_set để kiểm tra điều kiện O(1) thay vì O(V) của list
def dfs_matrix(matrix: list[list[int]], start_node: int) -> list[int]:
    n = len(matrix)
    visited_set: set[int] = set()
    order: list[int] = []
    stack: list[int] = [start_node]

    while stack:
        current = stack.pop()
        if current not in visited_set:
            visited_set.add(current)
            order.append(current)

            # Duyệt ngược để đỉnh có chỉ số nhỏ hơn nằm trên đỉnh stack và được pop trước
            for neighbor in reversed(range(n)):
                if matrix[current][neighbor] == 1 and neighbor not in visited_set:
                    stack.append(neighbor)
    return order


if __name__ == "__main__":
    print("BFS (Queue):", " -> ".join(bfs('A')))
    print("DFS (Recursive):", " -> ".join(dfs('A')))
    print("DFS (Iterative):", " -> ".join(dfs_iterative('A')))

    # Ma trận kề mẫu (4 đỉnh 0, 1, 2, 3)
    sample_matrix = [
        [0, 1, 1, 0],  # 0 nối với 1, 2
        [0, 0, 1, 0],  # 1 nối với 2
        [1, 0, 0, 1],  # 2 nối với 0, 3
        [0, 0, 0, 1]   # 3 có self-loop
    ]
    matrix_result = dfs_matrix(sample_matrix, 0)
    print("DFS (Matrix):", " -> ".join(str(node) for node in matrix_result))

