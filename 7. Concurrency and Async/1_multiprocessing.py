import os
import time
from concurrent.futures import ProcessPoolExecutor

# BÀI HỌC: ĐA TIẾN TRÌNH (MULTIPROCESSING) & VƯỢT QUA RÀO CẢN GIL
#
# BẢN CHẤT & GIA PHẢ:
# - GIL (Global Interpreter Lock) trong CPython:
#   Là một khóa mutex ngăn cản nhiều luồng (threads) cùng lúc thực thi mã bytecode Python.
#   Do đó, dù máy tính có 8 nhân hay 16 nhân CPU, Threading trong Python chỉ chạy trên 1 nhân duy nhất!
#
# GIẢI PHÁP VỚI MULTIPROCESSING:
# - Thay vì tạo luồng (threads), ta tạo ra các Tiến trình độc lập (Processes).
# - Mỗi Process có:
#   1. Một trình thông dịch Python (Python Interpreter) riêng biệt.
#   2. Không gian bộ nhớ RAM riêng biệt (không dùng chung biến, không lo Race Condition biến toàn cục).
#   3. Một GIL riêng biệt => Chạy SONG SONG THỰC SỰ (True Parallelism) trên tất cả các nhân CPU!
#
# KHI NÀO DÙNG MULTIPROCESSING?
# - Tác vụ nặng về tính toán CPU (CPU-Bound):
#   Xử lý ảnh/video, huấn luyện Machine Learning, nén file, mã hóa, tính toán ma trận lớn.
#
# QUY TẮC SỐNG CÒN TRÊN WINDOWS:
# - BẮT BUỘC phải đặt mã khởi chạy trong khối `if __name__ == '__main__':`
#   Vì Windows không có cơ chế `fork` như Linux mà dùng cơ chế `spawn` (khởi động lại script từ đầu).
#   Nếu thiếu dòng này, chương trình sẽ tự nhân bản vô hạn (Fork Bomb)!


def is_prime(n: int) -> bool:
    """Check if n is prime (Pure CPU-bound workload)."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def count_primes_in_range(start: int, end: int) -> int:
    """Count number of prime numbers in [start, end)."""
    count = 0
    for num in range(start, end):
        if is_prime(num):
            count += 1
    return count


def worker_task(chunk: tuple[int, int]) -> int:
    start, end = chunk
    # Print OS PID to prove workers run in distinct OS processes
    pid = os.getpid()
    res = count_primes_in_range(start, end)
    print(f" [PID {pid}] Processed range [{start:,} - {end:,}] -> Found {res:,} primes")
    return res


# Thực thi & So sánh hiệu năng
if __name__ == "__main__":
    print(f"Main Process PID: {os.getpid()}")
    print(f"Available CPU Cores: {os.cpu_count()}")

    # Divide problem into 4 chunks
    total_range = 1_000_000
    chunk_size = total_range // 4
    chunks = [
        (1, chunk_size),
        (chunk_size, chunk_size * 2),
        (chunk_size * 2, chunk_size * 3),
        (chunk_size * 3, total_range),
    ]

    # 1. Chạy tuần tự (Single Process)
    print("\n--- 1. Sequential Execution (1 Core) ---")
    start_seq = time.perf_counter()
    seq_results = [count_primes_in_range(s, e) for s, e in chunks]
    total_primes_seq = sum(seq_results)
    duration_seq = time.perf_counter() - start_seq
    print(f"Sequential Total: {total_primes_seq:,} primes in {duration_seq:.3f}s")

    # 2. Chạy song song đa tiến trình (ProcessPoolExecutor)
    print("\n--- 2. Parallel Execution with ProcessPoolExecutor (Multi-Core) ---")
    start_mp = time.perf_counter()
    with ProcessPoolExecutor(max_workers=4) as executor:
        mp_results = list(executor.map(worker_task, chunks))

    total_primes_mp = sum(mp_results)
    duration_mp = time.perf_counter() - start_mp
    print(f"Parallel Total:   {total_primes_mp:,} primes in {duration_mp:.3f}s")

    # Đánh giá độ tăng tốc (Speedup)
    speedup = duration_seq / duration_mp if duration_mp > 0 else 1.0
    print(f"\nSpeedup factor: {speedup:.2f}x faster using Multiprocessing!")
    assert total_primes_seq == total_primes_mp, "Both calculations must match!"
