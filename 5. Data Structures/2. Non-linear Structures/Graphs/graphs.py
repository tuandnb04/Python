# 5. Data Structures - Core: Đồ thị (Graphs)
# Khái niệm đồ thị và hai cách biểu diễn cốt lõi: Adjacency Matrix & Adjacency List
#
# 1. Khái niệm về Đồ thị (Graph Definition)
# - Đồ thị (Graph) là cấu trúc dữ liệu phi tuyến tính (non-linear) gồm tập hợp các đỉnh (vertices / nodes)
#   và các cạnh (edges) kết nối giữa các đỉnh.
# - Điểm khác biệt so với cấu trúc tuyến tính (Arrays, Linked Lists):
#   Đồ thị cho phép có nhiều đường đi khác nhau để di chuyển từ đỉnh này sang đỉnh khác.
# - Hai đỉnh được gọi là kề nhau (adjacent / neighbors) nếu tồn tại một cạnh nối trực tiếp giữa chúng.
#
# 2. Các bài toán mô hình hóa bằng Đồ thị
# - Mạng xã hội (Social Networks): Mỗi người dùng là một đỉnh, mối quan hệ bạn bè là cạnh.
#   Thuật toán đồ thị giúp gợi ý kết bạn.
# - Bản đồ & Dẫn đường (Maps & Navigation): Các địa điểm (thị trấn, trạm xe buýt) là đỉnh,
#   các tuyến đường là cạnh. Thuật toán tìm đường đi ngắn nhất (Dijkstra) giải quyết bài toán định tuyến.
# - Mạng Internet: Các trang web là đỉnh, các liên kết siêu văn bản (hyperlinks) là cạnh (PageRank).
# - Sinh học & Y học: Mô hình hóa mạng lưới nơ-ron thần kinh hoặc sự lây lan của dịch bệnh.

# 3. Phân loại Đồ thị (Graph Classifications)
# 3.1. Đồ thị vô hướng (Undirected Graph): Cạnh không có hướng, liên kết hai chiều đối xứng.
undirected_graph = {
    "A": ["B", "C", "D"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["A", "B"]
}

# 3.2. Đồ thị có hướng (Directed Graph / Digraph): Cạnh có hướng mũi tên xác định từ u đến v.
directed_graph = {
    "A": ["B"],
    "B": ["C"],
    "C": ["D"],
    "D": ["A"]
}

# 3.3. Đồ thị có trọng số (Weighted Graph): Mỗi cạnh mang một giá trị/chi phí (khoảng cách, cước phí).
weighted_graph = {
    "A": [("B", 3)],
    "B": [("C", 2)],
    "C": [("D", 1)],
    "D": [("A", 4)]
}

# 3.4. Đồ thị có hướng không chu trình (Directed Acyclic Graph - DAG):
# Không tồn tại đường đi khép kín xuất phát từ một đỉnh rồi quay lại chính nó.
# Ứng dụng trong lập lịch tác vụ phụ thuộc (Task Scheduling) và luồng commit của Git.
dag_graph = {
    "A": ["B"],
    "B": ["C", "D"],
    "C": ["D"],
    "D": ["E"],
    "E": []
}

print("Graph Classifications:")
print("Undirected neighbors of A:", undirected_graph["A"])
print("Directed edge from A:", directed_graph["A"])
print("Weighted edge from A:", weighted_graph["A"])
print("DAG downstream from B:", dag_graph["B"])


# 4. Biểu diễn bằng Ma trận kề (Adjacency Matrix)
# - Ma trận kề là mảng 2 chiều (kích thước V x V) lưu thông tin cạnh từ đỉnh i đến đỉnh j.
# - Đối với Đồ thị vô hướng: Ma trận luôn đối xứng qua đường chéo chính vì cạnh đi được cả 2 chiều.
# - Đối với Đồ thị có hướng: Ma trận không nhất thiết đối xứng, ô (i, j) = 1 thể hiện cạnh từ i đến j.
# - Đối với Đồ thị có trọng số: Giá trị tại ô (i, j) lưu trực tiếp trọng số của cạnh thay vì số 1.
# - Ưu điểm: Kiểm tra cạnh giữa 2 đỉnh bất kỳ cực nhanh O(1).
# - Nhược điểm: Chiếm bộ nhớ O(V^2), lãng phí bộ nhớ đối với đồ thị thưa (sparse graph).

# 4.1. Ma trận kề cho đồ thị vô hướng mẫu (Đỉnh A, B, C, D):
#     A  B  C  D
# A [ 0, 1, 1, 1 ]
# B [ 1, 0, 0, 1 ]
# C [ 1, 0, 0, 0 ]
# D [ 1, 1, 0, 0 ]
matrix_undirected = [
    [0, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0]
]

# 4.2. Ma trận kề cho đồ thị có hướng và có trọng số mẫu:
# A -> B (trọng số 3), B -> C (trọng số 2), C -> D (trọng số 1), D -> A (trọng số 4)
#     A  B  C  D
# A [ 0, 3, 0, 0 ]
# B [ 0, 0, 2, 0 ]
# C [ 0, 0, 0, 1 ]
# D [ 4, 0, 0, 0 ]
matrix_directed_weighted = [
    [0, 3, 0, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 1],
    [4, 0, 0, 0]
]


def print_matrix(matrix, labels):
    print("   " + "  ".join(labels))
    for i, row in enumerate(matrix):
        print(f"{labels[i]} {row}")


print("\nAdjacency Matrix (Undirected Graph):")
vertex_labels = ["A", "B", "C", "D"]
print_matrix(matrix_undirected, vertex_labels)
print("Has edge between A and B (O(1)):", matrix_undirected[0][1] == 1)

print("\nAdjacency Matrix (Directed & Weighted Graph):")
print_matrix(matrix_directed_weighted, vertex_labels)
print("Weight of edge A -> B:", matrix_directed_weighted[0][1])  # 3
print("Weight of edge D -> A:", matrix_directed_weighted[3][0])  # 4


# 5. Biểu diễn bằng Danh sách kề (Adjacency List)
# - Đồ thị thưa (Sparse Graph): Là đồ thị mà mỗi đỉnh chỉ kết nối với một lượng nhỏ các đỉnh khác.
# - Ma trận kề sẽ lãng phí nhiều bộ nhớ lưu các ô số 0 cho các cạnh không tồn tại.
# - Danh sách kề khắc phục nhược điểm này bằng cách chỉ lưu trữ danh sách các đỉnh kề thực tế.
# - Cấu trúc: Một mảng các đỉnh, mỗi đỉnh chứa một danh sách (hoặc linked list) các đỉnh kề với nó.
# - Bộ nhớ tiêu thụ: O(V + E) thay vì O(V^2), tối ưu vượt trội cho đồ thị thưa.

# 5.1. Danh sách kề cho đồ thị vô hướng:
# A (0): [1, 2, 3] -> B, C, D
# B (1): [0, 3]    -> A, D
# C (2): [0]       -> A
# D (3): [0, 1]    -> A, B
adj_list_undirected = {
    "A": ["B", "C", "D"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["A", "B"]
}

# 5.2. Danh sách kề cho đồ thị có hướng và có trọng số:
# Mỗi cạnh lưu cặp (đỉnh_đích, trọng_số)
adj_list_directed_weighted = {
    "A": [("B", 3)],
    "B": [("C", 2)],
    "C": [("D", 1)],
    "D": [("A", 4)]
}

print("\nAdjacency List (Undirected Graph):")
for vertex, neighbors in adj_list_undirected.items():
    print(f"Vertex {vertex} -> {neighbors}")

print("\nAdjacency List (Directed & Weighted Graph):")
for vertex, edges in adj_list_directed_weighted.items():
    formatted_edges = ", ".join(f"to {dest} (weight {w})" for dest, w in edges)
    print(f"Vertex {vertex} -> [{formatted_edges}]")


# 6. Chuyển đổi giữa Danh sách kề và Ma trận kề (Conversions)
# 6.1. Chuyển đổi từ Danh sách kề sang Ma trận kề: O(V^2 + E)
def adj_list_to_matrix(adj):
    nodes = list(adj.keys())
    node_to_idx = {node: i for i, node in enumerate(nodes)}
    n = len(nodes)
    matrix = [[0] * n for _ in range(n)]

    for node, neighbors in adj.items():
        u = node_to_idx[node]
        for neighbor in neighbors:
            if neighbor in node_to_idx:
                v = node_to_idx[neighbor]
                matrix[u][v] = 1

    return matrix, nodes


# 6.2. Chuyển đổi từ Ma trận kề sang Danh sách kề: O(V^2)
def matrix_to_adj_list(matrix, nodes):
    adj = {node: [] for node in nodes}
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                adj[nodes[i]].append(nodes[j])
    return adj


conv_matrix, conv_nodes = adj_list_to_matrix(adj_list_undirected)
print("\nConverted List to Matrix:")
print_matrix(conv_matrix, conv_nodes)

restored_list = matrix_to_adj_list(conv_matrix, conv_nodes)
print("\nMatrix restored back to List:")
print(restored_list)


# 7. So sánh hiệu năng giữa Adjacency Matrix và Adjacency List
# - Tiêu thụ không gian (Space Complexity):
#   + Adjacency Matrix: O(V^2) - Tốn bộ nhớ hơn, thích hợp cho Đồ thị dày (Dense Graph).
#   + Adjacency List:   O(V + E) - Tiết kiệm bộ nhớ, thích hợp cho Đồ thị thưa (Sparse Graph).
# - Kiểm tra có cạnh giữa u và v không (Edge Lookup):
#   + Adjacency Matrix: O(1) - Truy cập trực tiếp qua matrix[u][v].
#   + Adjacency List:   O(deg(u)) - Duyệt danh sách kề của đỉnh u.
# - Duyệt tất cả các đỉnh kề của một đỉnh (Find all neighbors):
#   + Adjacency Matrix: O(V) - Phải duyệt toàn bộ hàng u trong ma trận.
#   + Adjacency List:   O(deg(u)) - Duyệt trực tiếp các đỉnh kề thực tế.
print("\nGraph Complexity Summary:")
print("Space: Matrix O(V^2) vs List O(V + E)")
print("Edge Lookup: Matrix O(1) vs List O(deg(u))")
print("Iterate Neighbors: Matrix O(V) vs List O(deg(u))")
