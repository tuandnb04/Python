# Lập trình Bất đồng bộ hiện đại với asyncio.TaskGroup (Python 3.11+ PEP 654)
import asyncio

# => TẠI SAO TASKGROUP TỐT HƠN ASYNCIO.GATHER CŨ?
# 1. Structured Concurrency (Đồng quy có cấu trúc): Quản lý vòng đời task an toàn.
# 2. Tự động dọn dẹp (Auto-cleanup): Nếu 1 task bị lỗi, TaskGroup tự động hủy các task còn lại,
#    tránh rò rỉ tài nguyên và task "mồ côi" (orphaned tasks) mà gather() thường gặp.
# 3. Tích hợp hoàn hảo với ExceptionGroup để bắt mọi lỗi phát sinh đồng thời.

async def fetch_repository(repo_name: str, delay: float) -> str:
    print(f"Start fetching {repo_name}...")
    await asyncio.sleep(delay)  # Mô phỏng I/O non-blocking (tải mạng)
    print(f"Done fetching {repo_name}!")
    return f"Data of {repo_name}"

async def main():
    # Cách hiện đại (Python 3.11+): Dùng asyncio.TaskGroup()
    repos = [("pallets/flask", 0.05), ("psf/requests", 0.03), ("django/django", 0.07)]
    tasks = []
    
    async with asyncio.TaskGroup() as tg:
        for name, delay in repos:
            task = tg.create_task(fetch_repository(name, delay))
            tasks.append(task)

    results = [t.result() for t in tasks]
    print("All repositories fetched (TaskGroup):", results)

if __name__ == "__main__":
    asyncio.run(main())
