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

# Đồ thị có chu trình (Cyclic Graph) - Có ít nhất 1 đường đi khép kín quay lại đỉnh ban đầu
# Ví dụ chu trình: B -> C -> D -> B
cyclic_graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['D'],
    'D': ['B', 'E'],     # D nối ngược về B tạo chu trình khép kín
    'E': []
}

# Đồ thị có hướng không chu trình (Directed Acyclic Graph - DAG)
# - Cạnh có hướng và KHÔNG có chu trình (không thể xuất phát từ một đỉnh rồi quay lại chính nó)
# - Ứng dụng: Lập lịch tác vụ phụ thuộc (Task scheduling), Git commits, luồng biên dịch phần mềm
dag_graph = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

# Đồ thị không liên thông (Disconnected Graph) - Tồn tại từ 2 nhóm đỉnh độc lập trở lên
disconnected_graph = {
    # Nhóm 1: {A, B, C}
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B'],
    # Nhóm 2: {D, E} (hoàn toàn tách biệt, không có cạnh nào nối sang nhóm 1)
    'D': ['E'],
    'E': ['D']
}

print("Undirected neighbors of B:", undirected_graph['B']) # ['A', 'C', 'D']
print("Directed edges from D:", directed_graph['D'])       # ['B', 'E']
print("Weight of edge B -> D:", weighted_graph['B']['D'])  # 3
print("Cyclic loop check (D -> B):", 'B' in cyclic_graph['D']) # True
print("DAG downstream from B:", dag_graph['B'])            # ['C', 'D']
print("Disconnected components count:", len([k for k in disconnected_graph if k in ('A', 'D')])) # 2 groups


# 2. CÁC CÁCH BIỂU DIỄN ĐỒ THỊ TRÊN MÁY TÍNH

# Cách A: Adjacency Matrix (Ma trận kề) - Mảng 2 chiều kích thước V x V
# - Giá trị: 0/1 (đồ thị không trọng số) hoặc trọng số (đồ thị có trọng số)
# - Đường chéo chính (matrix[i][i]): Thể hiện khuyên / vòng lặp về chính nó (Self-loops)
# - Ưu điểm: Kiểm tra có cạnh giữa 2 đỉnh bất kỳ hay không mất O(1)
# - Nhược điểm:
#   + Tốn bộ nhớ O(V^2) (không hiệu quả cho đồ thị thưa vì lưu nhiều số 0 chiếm bộ nhớ)
#   + Tìm tất cả đỉnh kề của 1 đỉnh tốn O(V) vì phải duyệt toàn bộ hàng hoặc cột
# -> Thích hợp cho Dense Graph (đồ thị dày, nhiều cạnh)
#      A  B  C  D  (0: A, 1: B, 2: C, 3: D)
adj_matrix = [
    [0, 1, 1, 1],  # Đỉnh A nối với B, C, D
    [1, 0, 0, 1],  # Đỉnh B nối với A, D
    [1, 0, 0, 0],  # Đỉnh C nối với A
    [1, 1, 0, 0]   # Đỉnh D nối với A, B
]

print("Matrix: Has edge A-B? (O(1)):", adj_matrix[0][1] == 1) # True
# Tìm đỉnh kề của A trong ma trận: cần duyệt hết hàng 0 -> O(V)
neighbors_A_matrix = [chr(65 + j) for j, has_edge in enumerate(adj_matrix[0]) if has_edge]
print("Matrix: Neighbors of A (O(V)):", neighbors_A_matrix) # ['B', 'C', 'D']


# Cách B: Adjacency List (Danh sách kề)
# - Lưu danh sách các đỉnh kề thực tế của từng đỉnh
# - Ưu điểm: Tiết kiệm bộ nhớ O(V + E), duyệt danh sách đỉnh kề cực nhanh
# - Nhược điểm: Kiểm tra cạnh giữa 2 đỉnh u-v mất O(degree) (tệ nhất O(V) nếu đỉnh nối với tất cả đỉnh)
# -> Thích hợp cho Sparse Graph (đồ thị thưa, ít cạnh - dạng phổ biến nhất trong thực tế)

# B1. Dạng Dictionary / Hash Map (Phổ biến và linh hoạt nhất trong Python):
adj_list = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['A', 'B']
}
print("List (Dict): Neighbors of A:", adj_list['A']) # ['B', 'C', 'D']

# B2. Dạng Mảng 2 chiều (2D List / List of Lists theo chỉ số đỉnh 0..V-1):
# (0: A, 1: B, 2: C, 3: D)
adj_list_2d = [
    ['B', 'C', 'D'],  # Hàng xóm của A (index 0)
    ['A', 'D'],       # Hàng xóm của B (index 1)
    ['A'],            # Hàng xóm của C (index 2)
    ['A', 'B']        # Hàng xóm của D (index 3)
]
print("List (2D Array): Neighbors of A (index 0):", adj_list_2d[0]) # ['B', 'C', 'D']

