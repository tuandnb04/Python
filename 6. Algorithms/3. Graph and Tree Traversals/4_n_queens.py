# BÀI TOÁN XẾP N QUÂN HẬU (N-QUEENS PROBLEM - DFS & BACKTRACKING)
#
# 1. ĐẶT VẤN ĐỀ:
# - Đặt N quân hậu trên bàn cờ N x N sao cho không có 2 quân hậu nào tấn công lẫn nhau.
# - Hai quân hậu tấn công nhau nếu cùng hàng, cùng cột, hoặc cùng đường chéo.
#
# 2. MÔ HÌNH HÓA BẰNG DFS & BACKTRACKING:
# - Biểu diễn trạng thái: Mảng 1 chiều `queens` với `queens[row] = col` (quân hậu hàng `row` đặt ở cột `col`).
#   Vì mỗi hàng chỉ đặt đúng 1 quân hậu, ta không bao giờ gặp xung đột cùng hàng.
# - Duyệt cây không gian trạng thái (State Space Tree): Đặt thử từng cột cho từng hàng từ 0 đến N - 1.
# - Nhánh không an toàn sẽ bị cắt tỉa (Pruning) và quay lui (Backtrack).


# Cách 1: DFS tiếp cận cơ bản (Kiểm tra an toàn tuần tự qua từng quân hậu đã đặt)
def dfs_n_queens(n: int) -> list[list[int]]:
    """
    Solve N-Queens using basic DFS with sequential conflict checking.
    - Time complexity: O(N!)
    - Space complexity: O(N)
    """
    if n < 1:
        return []

    solutions: list[list[int]] = []

    def is_safe(queens: list[int], next_col: int) -> bool:
        next_row = len(queens)
        for row, col in enumerate(queens):
            # Kiểm tra cùng cột hoặc cùng đường chéo
            if col == next_col or abs(col - next_col) == abs(row - next_row):
                return False
        return True

    def dfs(queens: list[int]) -> None:
        if len(queens) == n:
            solutions.append(queens)
            return

        for col in range(n):
            if is_safe(queens, col):
                dfs(queens + [col])

    dfs([])
    return solutions


# Cách 2: Tối ưu hóa Backtracking với 3 Hash Sets kiểm tra va chạm O(1)
# - Quân hậu tại (row, col) bị khống chế bởi:
#   + Cột: col
#   + Đường chéo chính (\): row - col (hiệu số là hằng số)
#   + Đường chéo phụ (/): row + col (tổng số là hằng số)
# - Dùng in-place append/pop để tránh cấp phát bản sao list ở mỗi nhánh đệ quy
def solve_n_queens(n: int) -> list[list[int]]:
    """
    Solve N-Queens with O(1) conflict lookups using three sets and in-place backtracking.
    - Time complexity: O(N!)
    - Space complexity: O(N)
    """
    if n < 1:
        return []

    solutions: list[list[int]] = []
    cols: set[int] = set()
    diag_main: set[int] = set()  # row - col
    diag_anti: set[int] = set()  # row + col
    queens: list[int] = []

    def backtrack(row: int) -> None:
        if row == n:
            solutions.append(list(queens))
            return

        for col in range(n):
            if col in cols or (row - col) in diag_main or (row + col) in diag_anti:
                continue

            # Thử đặt quân hậu tại (row, col)
            cols.add(col)
            diag_main.add(row - col)
            diag_anti.add(row + col)
            queens.append(col)

            # Đệ quy xuống hàng tiếp theo
            backtrack(row + 1)

            # Quay lui (Backtrack): Hoàn tác trạng thái
            queens.pop()
            cols.remove(col)
            diag_main.remove(row - col)
            diag_anti.remove(row + col)

    backtrack(0)
    return solutions


# Hàm tiện ích trực quan hóa bàn cờ
def format_board(queen_positions: list[int]) -> list[str]:
    """Format queen column positions into an ASCII chessboard representation."""
    n = len(queen_positions)
    board: list[str] = []
    for col in queen_positions:
        row_str = " ".join("Q" if i == col else "." for i in range(n))
        board.append(row_str)
    return board


if __name__ == "__main__":
    n = 4
    solutions_basic = dfs_n_queens(n)
    solutions_optimized = solve_n_queens(n)

    print(f"Total solutions for {n}-Queens (Basic DFS)     : {len(solutions_basic)}")
    print(f"Total solutions for {n}-Queens (Optimized DFS) : {len(solutions_optimized)}")

    # Hiển thị tất cả các thế cờ nghiệm của 4-Queens
    for idx, sol in enumerate(solutions_optimized, start=1):
        print(f"\nSolution {idx} (Column positions: {sol}):")
        for row in format_board(sol):
            print(f"  {row}")

    # Thống kê nhanh số nghiệm với các giá trị N khác nhau:
    # N=1: 1, N=2: 0, N=3: 0, N=4: 2, N=8: 92
    print(f"\nSolution count for N=8: {len(solve_n_queens(8))} (Expected: 92)")
