# GRAPH DATA STRUCTURE (CẤU TRÚC DỮ LIỆU ĐỒ THỊ)
# - Nodes (Vertices / Đỉnh): Các thực thể (người dùng, thành phố, máy chủ...)
# - Edges (Cạnh): Mối liên kết/kết nối giữa các đỉnh
# - Adjacent Nodes (Đỉnh kề): Hai đỉnh được nối trực tiếp bằng một cạnh

# 1. PHÂN LOẠI ĐỒ THỊ

# Đồ thị vô hướng (Undirected Graph) - Kết nối 2 chiều đối xứng
undirected_graph = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['B', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

# Đồ thị có hướng (Directed Graph - Digraph) - Cạnh có chiều mũi tên xác định
directed_graph = {
    'A': ['B'],          # A -> B
    'B': ['C'],          # B -> C
    'C': ['D'],          # C -> D
    'D': ['B', 'E'],     # D -> B, D -> E
    'E': []
}

# Đồ thị có trọng số (Weighted Graph) - Mỗi cạnh mang một giá trị/chi phí (Distance, Cost, Bandwidth)
weighted_graph = {
    'A': {'B': 5},
    'B': {'C': 2, 'D': 3},
    'D': {'E': 4}
}

print("Undirected neighbors of B:", undirected_graph['B']) # ['A', 'C', 'D']
print("Directed edges from D:", directed_graph['D'])       # ['B', 'E']
print("Weight of edge B -> D:", weighted_graph['B']['D'])  # 3


# 2. CÁC CÁCH BIỂU DIỄN ĐỒ THỊ TRÊN MÁY TÍNH

# Cách A: Adjacency Matrix (Ma trận kề) - Mảng 2 chiều kích thước V x V
# - Ưu điểm: Kiểm tra cạnh giữa 2 đỉnh bất kỳ mất O(1)
# - Nhược điểm: Tốn bộ nhớ O(V^2) -> Thích hợp cho Dense Graph (đồ thị dày, nhiều cạnh)
#      A  B  C  D  (0: A, 1: B, 2: C, 3: D)
adj_matrix = [
    [0, 1, 1, 1],  # Đỉnh A nối với B, C, D
    [1, 0, 0, 1],  # Đỉnh B nối với A, D
    [1, 0, 0, 0],  # Đỉnh C nối với A
    [1, 1, 0, 0]   # Đỉnh D nối với A, B
]

print("Matrix: Has edge A-B? (O(1)):", adj_matrix[0][1] == 1) # True

# Cách B: Adjacency List (Danh sách kề) - Dictionary / Hash Map (Phổ biến nhất trong Python)
# - Ưu điểm: Tiết kiệm bộ nhớ O(V + E), duyệt danh sách đỉnh kề cực nhanh
# - Nhược điểm: Kiểm tra cạnh mất O(degree) -> Thích hợp cho Sparse Graph (đồ thị thưa, ít cạnh)
adj_list = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['A', 'B']
}

print("List: Neighbors of A:", adj_list['A']) # ['B', 'C', 'D']
