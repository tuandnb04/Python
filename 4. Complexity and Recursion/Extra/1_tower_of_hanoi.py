# 1. Bài toán Tháp Hà Nội (Tower of Hanoi) & Đệ quy Phân nhánh
# Bài toán kinh điển minh họa cho độ phức tạp hàm mũ O(2^n) và kỹ thuật Chia để trị (Divide and Conquer):
# - Đề bài: Có 3 cọc (Source, Destination, Auxiliary) và n đĩa kích thước khác nhau xếp chồng tại cọc Source.
# - Mục tiêu: Chuyển toàn bộ n đĩa từ cọc Source sang cọc Destination.
# - Ràng buộc:
#   1. Mỗi lần chỉ được di chuyển đúng 1 đĩa trên cùng.
#   2. Không bao giờ được đặt đĩa lớn hơn lên trên đĩa nhỏ hơn.

# 2. Chiến lược giải đệ quy (Recursive Strategy)
# Để chuyển n đĩa từ Source sang Destination dùng Auxiliary:
# - Bước 1: Chuyển (n - 1) đĩa trên cùng từ Source sang Auxiliary (dùng Destination làm cọc phụ).
# - Bước 2: Chuyển đĩa thứ n (đĩa lớn nhất) trực tiếp từ Source sang Destination.
# - Bước 3: Chuyển (n - 1) đĩa từ Auxiliary sang Destination (dùng Source làm cọc phụ).

def hanoi_solver(n: int) -> list[str]:
    """
    Giải bài toán Tháp Hà Nội và ghi lại toàn bộ trạng thái của 3 cọc sau mỗi bước chuyển.
    - Time Complexity: O(2^n) phép di chuyển đĩa thuần túy (chính xác: 2^n - 1 bước).
    - Space Complexity: O(n) độ sâu ngăn xếp Call Stack.
    """
    # Khởi tạo 3 cọc: Cọc 0 có các đĩa từ n giảm dần về 1, Cọc 1 và 2 ban đầu rỗng
    rods: list[list[int]] = [list(range(n, 0, -1)), [], []]
    snapshots: list[str] = []

    def record_state() -> None:
        snapshots.append(f"Rod A: {rods[0]} | Rod B: {rods[1]} | Rod C: {rods[2]}")

    def solve(k: int, src: int, dst: int, aux: int) -> None:
        if k == 0:
            return
        # Bước 1: Chuyển k - 1 đĩa từ src sang aux
        solve(k - 1, src, aux, dst)

        # Bước 2: Chuyển đĩa lớn nhất từ src sang dst
        rods[dst].append(rods[src].pop())
        record_state()

        # Bước 3: Chuyển k - 1 đĩa từ aux sang dst
        solve(k - 1, aux, dst, src)

    record_state()  # Ghi trạng thái ban đầu
    solve(n, 0, 2, 1)  # Chuyển n đĩa từ cọc 0 (A) sang cọc 2 (C) qua cọc 1 (B)
    return snapshots

print("Tower of Hanoi simulation for n = 3 disks:")
steps = hanoi_solver(3)
for step_no, state in enumerate(steps):
    if step_no == 0:
        print(f"Initial: {state}")
    else:
        print(f"Step {step_no:2d}: {state}")

print(f"\nTotal moves for n=3: {len(steps) - 1} (Formula: 2^3 - 1 = 7)")
