# 1. Adjacency Matrix (Ma trận kề) - 2D List (kích thước V x V)
# - Ưu điểm: Kiểm tra cạnh tồn tại giữa 2 đỉnh chỉ mất O(1)
# - Nhược điểm: Tốn bộ nhớ O(V^2) -> Thích hợp nhất cho Dense Graph (đồ thị dày, nhiều cạnh)
#      A  B  C  D  (0: A, 1: B, 2: C, 3: D)
adj_matrix = [
    [0, 1, 1, 1],  # Đỉnh A nối với B, C, D
    [1, 0, 0, 1],  # Đỉnh B nối với A, D
    [1, 0, 0, 0],  # Đỉnh C nối với A
    [1, 1, 0, 0]   # Đỉnh D nối với A, B
]

# Kiểm tra trực tiếp cạnh giữa A (0) và B (1) -> O(1)
print("Matrix: Has edge A-B? (O(1)):", adj_matrix[0][1] == 1) # True

# 2. Adjacency List (Danh sách kề) - Dictionary hoặc List of lists
# - Ưu điểm: Tiết kiệm bộ nhớ O(V + E), duyệt danh sách đỉnh kề cực nhanh
# - Nhược điểm: Kiểm tra cạnh mất O(degree) -> Thích hợp cho Sparse Graph (đồ thị thưa, ít cạnh)
adj_list = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['A', 'B']
}

print("List: Neighbors of A:", adj_list['A']) # ['B', 'C', 'D']
