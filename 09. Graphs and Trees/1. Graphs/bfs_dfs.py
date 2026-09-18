from collections import deque

# Đồ thị / Cây mẫu dạng Adjacency List
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [], 'E': [], 'F': [], 'G': []
}

# 1. Breadth-First Search (BFS) - Dùng Queue (FIFO)
# - Duyệt theo từng tầng (level-by-level)
# - Dùng tìm đường đi ngắn nhất (shortest path) trên đồ thị không trọng số
def bfs(start_node):
    visited = []
    queue = deque([start_node])
    seen = {start_node}

    while queue:
        node = queue.popleft()        # Dequeue phần tử đầu hàng đợi
        visited.append(node)
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)# Enqueue vào cuối hàng đợi
    return visited

# 2. Depth-First Search (DFS) - Dùng Đệ quy (hoặc Stack LIFO)
# - Đi sâu hết từng nhánh trước khi quay lui (backtracking)
# - Thích hợp giải mê cung, phát hiện chu trình (cycle detection)
def dfs(node, visited=None):
    if visited is None:
        visited = []
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)
    return visited

print("BFS (Queue):", " -> ".join(bfs('A'))) # A -> B -> C -> D -> E -> F -> G
print("DFS (Stack):", " -> ".join(dfs('A'))) # A -> B -> D -> E -> C -> F -> G
