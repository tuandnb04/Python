# 1. Các thành phần cơ bản của Đồ thị (Graph):
# - Nodes (Vertices / Đỉnh): Thực thể (người dùng, thành phố, máy tính...)
# - Edges (Cạnh): Mối liên kết/kết nối giữa các đỉnh
# - Adjacent Nodes (Đỉnh kề): Hai đỉnh được kết nối trực tiếp bởi một cạnh

# 2. Đồ thị vô hướng (Undirected Graph) - Kết nối 2 chiều
undirected_graph = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['B', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

# 3. Đồ thị có hướng (Directed Graph - Digraph) - Cạnh có chiều xác định
# Nếu có chu trình (ví dụ B -> C -> D -> B) thì gọi là Cyclic Graph
# Nếu không có chu trình thì gọi là Directed Acyclic Graph (DAG)
directed_graph = {
    'A': ['B'],          # A -> B
    'B': ['C'],          # B -> C
    'C': ['D'],          # C -> D
    'D': ['B', 'E'],     # D -> B, D -> E
    'E': []
}

# 4. Đồ thị có trọng số (Weighted Graph) - Mỗi cạnh có giá trị/chi phí
weighted_graph = {
    'A': {'B': 5},
    'B': {'C': 2, 'D': 3},
    'D': {'E': 4}
}

print("Undirected neighbors of B:", undirected_graph['B']) # ['A', 'C', 'D']
print("Directed edges from D:", directed_graph['D'])       # ['B', 'E']
print("Weight of edge B -> D:", weighted_graph['B']['D'])  # 3
