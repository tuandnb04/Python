import threading
import time
from concurrent.futures import ThreadPoolExecutor

# BÀI HỌC: ĐA LUỒNG (THREADING) & ĐỒNG BỘ HÓA TRONG PYTHON
#
# BẢN CHẤT & GIA PHẢ:
# - Tiến trình (Process): Một chương trình đang chạy, có không gian bộ nhớ RAM độc lập.
# - Luồng (Thread): Là đơn vị thực thi nhỏ nhất bên trong một Tiến trình.
#   Các luồng trong cùng một tiến trình CHIA SẺ CHUNG không gian bộ nhớ.
#
# KHI NÀO NÊN DÙNG THREADING TRONG PYTHON?
# - Tác vụ I/O-Bound (Nghẽn vào/ra): Đọc/ghi file, tải trang web, gọi API mạng, truy vấn cơ sở dữ liệu.
#   Khi một luồng chờ mạng/ổ đĩa phản hồi, CPython sẽ nhả GIL (Global Interpreter Lock)
#   để luồng khác được chạy => Tăng tốc độ chương trình vượt bậc!
# - Tác vụ CPU-Bound (Nghẽn tính toán): Threading KHÔNG giúp tăng tốc trong CPython tiêu chuẩn
#   vì bị khóa bởi GIL (sẽ học giải pháp ở bài Multiprocessing tiếp theo).


# 1. Tạo và khởi chạy luồng thủ công với threading.Thread

def download_file(file_name: str, delay: float) -> None:
    # Simulate network I/O latency
    print(f"[{threading.current_thread().name}] Start downloading {file_name}...")
    time.sleep(delay)
    print(f"[{threading.current_thread().name}] Finished downloading {file_name}!")


def demo_manual_threads() -> None:
    print("--- 1. Manual Thread Creation (Sequential vs Concurrent) ---")
    start = time.perf_counter()

    # Create two independent worker threads
    t1 = threading.Thread(target=download_file, args=("image1.png", 0.5), name="Worker-1")
    t2 = threading.Thread(target=download_file, args=("video2.mp4", 0.5), name="Worker-2")

    t1.start()
    t2.start()

    # Wait for both threads to finish
    t1.join()
    t2.join()

    duration = time.perf_counter() - start
    print(f"Total download time for 2 files: {duration:.3f}s (vs 1.0s if sequential)")


# 2. Bẫy tranh chấp dữ liệu (Race Condition) & threading.Lock
# Khi nhiều luồng cùng đọc và ghi vào một biến chung (Shared State) mà không có
# cơ chế bảo vệ, dữ liệu sẽ bị sai lệch nghiêm trọng do luồng bị ngắt giữa chừng.

shared_balance = 0
lock = threading.Lock()  # Mutex lock


def unsafe_deposit(amount: int, iterations: int) -> None:
    global shared_balance
    for _ in range(iterations):
        # Read-Modify-Write is non-atomic
        temp = shared_balance
        time.sleep(0.000001)  # Force thread context switch
        shared_balance = temp + amount


def safe_deposit(amount: int, iterations: int) -> None:
    global shared_balance
    for _ in range(iterations):
        # Critical section protected by lock
        with lock:
            temp = shared_balance
            time.sleep(0.000001)
            shared_balance = temp + amount


def demo_race_condition() -> None:
    global shared_balance
    print("\n--- 2. Race Condition & Threading Lock ---")

    # Unsafe trial
    shared_balance = 0
    threads = [threading.Thread(target=unsafe_deposit, args=(1, 50)) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Unsafe Balance: {shared_balance} (Expected: 200 => Lost updates due to race condition)")

    # Safe trial with mutex
    shared_balance = 0
    threads = [threading.Thread(target=safe_deposit, args=(1, 50)) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"Safe Balance with Lock: {shared_balance} (Exactly 200)")


# 3. Quản lý bể luồng hiện đại với ThreadPoolExecutor
# Thay vì tự tạo từng Thread thủ công, chuẩn công nghiệp luôn dùng ThreadPoolExecutor:
# - Tự động tái sử dụng các luồng (Thread reuse).
# - Giới hạn số luồng tối đa để không làm cạn kiệt tài nguyên hệ thống.
# - Dễ dàng lấy kết quả trả về thông qua Future object.

def fetch_web_page(url: str) -> str:
    # Simulate network request
    time.sleep(0.1)
    return f"Response 200 OK from {url}"


def demo_thread_pool() -> None:
    print("\n--- 3. Modern ThreadPoolExecutor ---")
    urls = [
        "https://api.github.com",
        "https://python.org",
        "https://pypi.org",
        "https://docs.python.org",
    ]

    # Pool with at most 3 worker threads
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(fetch_web_page, urls)
        for res in results:
            print(" ->", res)


# Thực thi & Kiểm chứng
if __name__ == "__main__":
    demo_manual_threads()
    demo_race_condition()
    demo_thread_pool()
