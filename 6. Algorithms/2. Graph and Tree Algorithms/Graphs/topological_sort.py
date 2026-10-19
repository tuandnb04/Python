from collections import deque

# BÀI HỌC: SẮP XẾP TOPO (TOPOLOGICAL SORT) & PHÁT HIỆN CHU TRÌNH TRÊN DAG
#
# BẢN CHẤT & GIA PHẢ:
# - Áp dụng ĐỘC QUYỀN trên: Đồ thị có hướng không có chu trình (DAG - Directed Acyclic Graph).
#   Nếu đồ thị có chu trình (Cycle), Topological Sort là BẤT KHẢ THI!
# - Định nghĩa:
#   Topological Sort là một thứ tự sắp xếp tuyến tính của tất cả các đỉnh sao cho:
#   Với mọi cạnh có hướng từ u -> v, đỉnh u luôn luôn xuất hiện TRƯỚC đỉnh v trong thứ tự sắp xếp.
#
# ỨNG DỤNG THỰC TẾ:
# 1. Quản lý phụ thuộc gói phần mềm (Package Dependency Resolution trong pip, npm, apt).
# 2. Lập lịch thực thi tác vụ (Task Scheduling trong Apache Airflow, CI/CD pipelines, Makefile).
# 3. Đăng ký môn học theo điều kiện môn tiên quyết (Course Prerequisites).


# 1. Thuật toán Kahn (dựa trên BFS & Bán bậc vào In-degree)
# Ý tưởng:
# 1. Đếm bán bậc vào (In-degree) của mọi đỉnh (số lượng cạnh trỏ tới nó).
# 2. Đưa các đỉnh có In-degree = 0 (không phụ thuộc vào ai) vào một hàng đợi (Queue).
# 3. Lấy từng đỉnh ra khỏi Queue, thêm vào kết quả, và giảm In-degree của các đỉnh kề nó đi 1.
# 4. Nếu đỉnh kề giảm về 0, đưa tiếp vào Queue.
# 5. Nếu số đỉnh trong kết quả < tổng số đỉnh đồ thị => Đồ thị CÓ CHU TRÌNH!

def topological_sort_kahn(num_nodes: int, edges: list[tuple[int, int]]) -> list[int] | None:
    """
    Topological sort using Kahn's algorithm (BFS).
    - Time complexity: O(V + E)
    - Space complexity: O(V + E)
    Returns: list of ordered nodes, or None if a cycle is detected.
    """
    adj: dict[int, list[int]] = {i: [] for i in range(num_nodes)}
    in_degree: list[int] = [0] * num_nodes

    # Build adjacency list and in-degree array
    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1

    # Queue all nodes with 0 in-degree
    queue = deque([i for i in range(num_nodes) if in_degree[i] == 0])
    topo_order: list[int] = []

    while queue:
        curr = queue.popleft()
        topo_order.append(curr)

        # Reduce in-degree of all adjacent nodes
        for neighbor in adj[curr]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Cycle detected if processed count does not equal total nodes
    if len(topo_order) != num_nodes:
        return None

    return topo_order


# 2. Thuật toán DFS tô màu 3 trạng thái (3-Color DFS)
# Trạng thái các đỉnh:
# - WHITE (0): Chưa thăm
# - GRAY (1): Đang thăm (nằm trong Call Stack đệ quy hiện tại). Nếu gặp lại GRAY => CÓ CHU TRÌNH!
# - BLACK (2): Đã duyệt xong hoàn toàn cùng tất cả các con của nó.

def topological_sort_dfs(num_nodes: int, edges: list[tuple[int, int]]) -> list[int] | None:
    """
    Topological sort using DFS (reversed post-order) with cycle detection.
    - Time complexity: O(V + E)
    - Space complexity: O(V + E)
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    state = [WHITE] * num_nodes
    adj: dict[int, list[int]] = {i: [] for i in range(num_nodes)}
    for u, v in edges:
        adj[u].append(v)

    order: list[int] = []
    has_cycle = False

    def dfs(node: int) -> None:
        nonlocal has_cycle
        if has_cycle:
            return

        state[node] = GRAY  # Currently visiting
        for neighbor in adj[node]:
            if state[neighbor] == GRAY:
                has_cycle = True  # Back edge found -> cycle
                return
            elif state[neighbor] == WHITE:
                dfs(neighbor)

        state[node] = BLACK  # Finished visiting
        order.append(node)

    for i in range(num_nodes):
        if state[i] == WHITE:
            dfs(i)
            if has_cycle:
                return None

    order.reverse()  # Reverse post-order to get topological sort
    return order


# Thực thi & Kiểm chứng
if __name__ == "__main__":
    # Đồ thị 1: DAG hợp lệ gồm 6 tác vụ (0 -> 5)
    # Ví dụ môn học: 5 -> 2, 5 -> 0, 4 -> 0, 4 -> 1, 2 -> 3, 3 -> 1
    num_nodes_1 = 6
    edges_dag = [
        (5, 2), (5, 0),
        (4, 0), (4, 1),
        (2, 3), (3, 1)
    ]

    print("--- 1. Valid DAG Topological Sort ---")
    order_kahn = topological_sort_kahn(num_nodes_1, edges_dag)
    order_dfs = topological_sort_dfs(num_nodes_1, edges_dag)
    print("Kahn's (BFS) Topo Order:", order_kahn)
    print("DFS Topo Order:        ", order_dfs)

    # Đồ thị 2: Có chu trình (Deadlock / Circular Dependency)
    # 0 -> 1 -> 2 -> 0
    num_nodes_2 = 3
    edges_cyclic = [(0, 1), (1, 2), (2, 0)]

    print("\n--- 2. Graph with Cycle Detection ---")
    cyclic_result = topological_sort_kahn(num_nodes_2, edges_cyclic)
    print("Kahn result on cyclic graph:", cyclic_result)
    assert cyclic_result is None, "Kahn algorithm must detect cycle!"

    cyclic_result_dfs = topological_sort_dfs(num_nodes_2, edges_cyclic)
    print("DFS result on cyclic graph: ", cyclic_result_dfs)
    assert cyclic_result_dfs is None, "DFS algorithm must detect cycle!"
