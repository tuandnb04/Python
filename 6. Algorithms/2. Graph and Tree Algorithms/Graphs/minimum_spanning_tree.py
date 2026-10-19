import heapq

# BÀI HỌC: CÂY KHUNG NHỎ NHẤT (MINIMUM SPANNING TREE - MST) & DSU
#
# BẢN CHẤT & GIA PHẢ:
# - Cây khung (Spanning Tree) của đồ thị vô hướng liên thông G=(V, E) là một đồ thị con
#   chứa TẤT CẢ các đỉnh V, là một CÂY (liên thông và KHÔNG có chu trình), gồm đúng |V| - 1 cạnh.
# - Cây khung nhỏ nhất (MST) là cây khung có TỔNG TRỌNG SỐ các cạnh là NHỎ NHẤT.
#
# HAI THUẬT TOÁN KINH ĐIỂN:
# 1. Thuật toán Kruskal (Dựa trên cạnh & Cấu trúc DSU):
#    - Chiến lược Tham lam (Greedy): Sắp xếp toàn bộ cạnh theo trọng số tăng dần.
#    - Lần lượt chọn cạnh nhỏ nhất, dùng Disjoint Set Union (DSU) để kiểm tra xem 2 đầu mút
#      đã thuộc cùng một tập hợp hay chưa. Nếu chưa -> thêm vào MST và gộp 2 tập hợp lại.
#    - Độ phức tạp: O(E log E) hoặc O(E log V).
#
# 2. Thuật toán Prim (Dựa trên đỉnh & Min-Heap):
#    - Bắt đầu từ 1 đỉnh tùy ý, luôn mở rộng cây khung bằng cách chọn cạnh nhẹ nhất
#      nối giữa một đỉnh ĐÃ trong cây với một đỉnh CHƯA trong cây (dùng Priority Queue).
#    - Độ phức tạp: O(E log V).


# 1. Cấu trúc dữ liệu Tập hợp rời nhau (Disjoint Set Union - DSU)
# Bao gồm 2 kỹ thuật tối ưu hóa tối cao:
# 1. Nén đường đi (Path Compression): Khi tìm đại diện find(x), trỏ trực tiếp x lên nút gốc.
# 2. Gộp theo cấp bậc (Union by Rank): Gộp cây thấp hơn vào gốc của cây cao hơn để hạn chế chiều cao.
# => Giúp mọi thao tác đạt độ phức tạp gần như hằng số: O(α(V)) (hàm ngược Ackermann).

class DisjointSetUnion:
    def __init__(self, size: int) -> None:
        self.parent: list[int] = list(range(size))
        self.rank: list[int] = [0] * size

    def find(self, i: int) -> int:
        """Find root representative with Path Compression."""
        if self.parent[i] == i:
            return i
        # Flatten tree directly to root
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x: int, y: int) -> bool:
        """
        Merge sets containing x and y using Union by Rank.
        Returns True if merged successfully, False if already in same set (cycle).
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in same set -> cycle

        # Attach smaller rank tree under larger rank tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


# 2. Thuật toán Kruskal

def kruskal_mst(num_nodes: int, edges: list[tuple[int, int, int]]) -> tuple[int, list[tuple[int, int, int]]]:
    """
    Kruskal's algorithm for MST.
    edges: list of (u, v, weight)
    Returns: (total_weight, mst_edges)
    """
    # Sort all edges by weight ascending: O(E log E)
    sorted_edges = sorted(edges, key=lambda edge: edge[2])

    dsu = DisjointSetUnion(num_nodes)
    mst_edges: list[tuple[int, int, int]] = []
    total_weight = 0

    # Greedily pick smallest non-cyclic edge
    for u, v, weight in sorted_edges:
        if dsu.union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight
            if len(mst_edges) == num_nodes - 1:
                break

    return total_weight, mst_edges


# 3. Thuật toán Prim

def prim_mst(num_nodes: int, edges: list[tuple[int, int, int]], start_node: int = 0) -> tuple[int, list[tuple[int, int, int]]]:
    """
    Prim's algorithm for MST using Min-Heap (Priority Queue).
    - Time complexity: O(E log V)
    """
    # Build adjacency list: u -> list of (neighbor, weight)
    adj: dict[int, list[tuple[int, int]]] = {i: [] for i in range(num_nodes)}
    for u, v, weight in edges:
        adj[u].append((v, weight))
        adj[v].append((u, weight))

    visited = [False] * num_nodes
    min_heap: list[tuple[int, int, int]] = []  # (weight, from_node, to_node)
    mst_edges: list[tuple[int, int, int]] = []
    total_weight = 0

    # Start from start_node
    visited[start_node] = True
    for neighbor, weight in adj[start_node]:
        heapq.heappush(min_heap, (weight, start_node, neighbor))

    while min_heap and len(mst_edges) < num_nodes - 1:
        weight, u, v = heapq.heappop(min_heap)

        if visited[v]:
            continue

        # Add edge to MST
        visited[v] = True
        mst_edges.append((u, v, weight))
        total_weight += weight

        # Push neighboring edges
        for neighbor, next_weight in adj[v]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (next_weight, v, neighbor))

    return total_weight, mst_edges


# Thực thi & Kiểm chứng
if __name__ == "__main__":
    # Đồ thị vô hướng 5 đỉnh (0 -> 4) với 7 cạnh có trọng số
    num_nodes = 5
    graph_edges = [
        (0, 1, 2),  # Cạnh (0, 1) trọng số 2
        (0, 3, 6),  # Cạnh (0, 3) trọng số 6
        (1, 2, 3),  # Cạnh (1, 2) trọng số 3
        (1, 3, 8),  # Cạnh (1, 3) trọng số 8
        (1, 4, 5),  # Cạnh (1, 4) trọng số 5
        (2, 4, 7),  # Cạnh (2, 4) trọng số 7
        (3, 4, 9),  # Cạnh (3, 4) trọng số 9
    ]

    print("--- 1. Kruskal's MST ---")
    kruskal_cost, kruskal_tree = kruskal_mst(num_nodes, graph_edges)
    print("Kruskal Total Weight:", kruskal_cost)
    print("Kruskal Tree Edges:  ", kruskal_tree)

    print("\n--- 2. Prim's MST ---")
    prim_cost, prim_tree = prim_mst(num_nodes, graph_edges)
    print("Prim Total Weight:   ", prim_cost)
    print("Prim Tree Edges:     ", prim_tree)

    assert kruskal_cost == prim_cost, "Both algorithms must find the exact same minimum weight!"
    print("\nVerification: Both Kruskal and Prim match minimum weight =", kruskal_cost)
