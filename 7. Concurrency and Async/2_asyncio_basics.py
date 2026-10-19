import asyncio
import time

# BÀI HỌC: LẬP TRÌNH BẤT ĐỒNG BỘ VỚI ASYNCIO (ASYNCHRONOUS I/O)
#
# BẢN CHẤT & GIA PHẢ:
# - So sánh 3 mô hình xử lý song song/đồng thời trong Python:
#   1. Multiprocessing: Đa tiến trình, đa nhân CPU, đa vùng nhớ (Dành cho CPU-Bound).
#   2. Threading: Đa luồng do Hệ điều hành quản lý (Preemptive Multitasking), chia sẻ RAM (Dành cho I/O-Bound).
#   3. Asyncio: Đơn luồng (Single-Thread), Bất đồng bộ do Ứng dụng tự quản lý (Cooperative Multitasking).
#      Một luồng duy nhất có thể phục vụ hàng chục ngàn kết nối mạng cùng lúc (High Concurrency)!
#
# CÁC KHÁI NIỆM CỐT LÕI:
# - Event Loop (Vòng lặp sự kiện): Trái tim của asyncio, liên tục theo dõi và điều phối các tác vụ.
# - Coroutine (`async def`): Hàm có khả năng tạm dừng (pause) tại điểm `await` và nhường CPU
#   cho tác vụ khác, sau đó tự động tiếp tục khi dữ liệu I/O đã sẵn sàng.
# - Từ khóa `await`: Điểm nhường quyền điều khiển về cho Event Loop.
# - BẪY CHẾT NGƯỜI: Tuyệt đối KHÔNG gọi các hàm Blocking đồng bộ (như `time.sleep()`, `requests.get()`)
#   bên trong coroutine vì nó sẽ đóng băng toàn bộ Event Loop! Luôn dùng hàm async tương ứng (như `asyncio.sleep()`, `httpx`).


# 1. Từ khóa async def & await cơ bản

async def fetch_api_data(service_name: str, delay: float) -> dict[str, str | float]:
    """Simulate asynchronous API fetch."""
    print(f" -> [Start] Requesting data from {service_name}...")
    # asyncio.sleep is non-blocking: yields control back to event loop
    await asyncio.sleep(delay)
    print(f" <- [Done] Received response from {service_name}!")
    return {"service": service_name, "latency_sec": delay}


# 2. Chạy đồng thời với asyncio.gather()
# gather() nhận vào nhiều coroutines, đưa vào Event loop và chạy đồng thời,
# gom toàn bộ kết quả trả về thành một danh sách (list) theo đúng thứ tự truyền vào.

async def demo_gather() -> None:
    print("--- 1. Concurrent execution with asyncio.gather() ---")
    start = time.perf_counter()

    # Call 3 microservices concurrently
    results = await asyncio.gather(
        fetch_api_data("AuthService", 0.3),
        fetch_api_data("PaymentService", 0.4),
        fetch_api_data("InventoryService", 0.2),
    )

    duration = time.perf_counter() - start
    print(f"Results collected: {results}")
    print(f"Total time with gather: {duration:.3f}s (Max latency ~0.4s vs 0.9s if sequential)")


# 3. Cấu trúc đồng thời hiện đại với asyncio.TaskGroup (Python 3.11+)
# Kỹ thuật Structured Concurrency (Đồng thời có cấu trúc):
# - Dùng cú pháp `async with asyncio.TaskGroup() as tg:`
# - Ưu điểm vượt trội so với gather: Nếu 1 task bị văng lỗi (Exception), TaskGroup sẽ
#   TỰ ĐỘNG hủy bỏ (cancel) an toàn tất cả các task còn lại trong nhóm, tránh rò rỉ tác vụ ngầm!

async def query_database(query_id: int) -> str:
    # Simulate DB query latency
    await asyncio.sleep(0.15)
    return f"Query-{query_id} OK"


async def demo_task_group() -> None:
    print("\n--- 2. Modern Structured Concurrency with TaskGroup (Python 3.11+) ---")
    tasks = []

    async with asyncio.TaskGroup() as tg:
        for i in range(1, 4):
            # Schedule coroutines inside the task group
            task = tg.create_task(query_database(i))
            tasks.append(task)

    # When leaving 'async with', all tasks are guaranteed complete
    for task in tasks:
        print("Task result:", task.result())


# 4. So sánh Blocking (time.sleep) vs Non-blocking (asyncio.sleep)

async def blocking_task(idx: int) -> None:
    # Anti-pattern: Blocking call freezes entire thread
    time.sleep(0.1)
    print(f"Blocking task {idx} done")


async def non_blocking_task(idx: int) -> None:
    # Proper async non-blocking sleep
    await asyncio.sleep(0.1)
    print(f"Non-blocking task {idx} done")


async def demo_blocking_vs_non_blocking() -> None:
    print("\n--- 3. Blocking vs Non-Blocking Comparison ---")

    print("[Testing Blocking time.sleep in Coroutines]:")
    start = time.perf_counter()
    await asyncio.gather(blocking_task(1), blocking_task(2), blocking_task(3))
    print(f"Time taken (Serialized by blocking call): {time.perf_counter() - start:.3f}s (~0.3s)")

    print("\n[Testing Non-Blocking asyncio.sleep in Coroutines]:")
    start = time.perf_counter()
    await asyncio.gather(non_blocking_task(1), non_blocking_task(2), non_blocking_task(3))
    print(f"Time taken (Truly concurrent): {time.perf_counter() - start:.3f}s (~0.1s)")


# Hàm main điều phối (Entry Point)
async def main() -> None:
    await demo_gather()
    await demo_task_group()
    await demo_blocking_vs_non_blocking()


if __name__ == "__main__":
    asyncio.run(main())
