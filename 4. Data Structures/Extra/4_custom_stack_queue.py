# Custom Generic Stack & Queue (Tự xây dựng cấu trúc dữ liệu bọc class)
# - Ghi chú: Thường dùng để học bản chất OOP, Generic Type Hints hoặc giải bài tập phỏng vấn.
# - Trong thực tế dự án Python:
#     + Stack: Dùng trực tiếp 'list' với .append() và .pop() là chuẩn và nhanh nhất.
#     + Queue: Dùng 'collections.deque' có sẵn với C-level implementation tối ưu vượt trội.

from collections import deque

# 1. Generic Stack tự định nghĩa với cú pháp PEP 695 (Python 3.12+)
class TypedStack[T]:
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T:
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)


# 2. Generic Queue tự định nghĩa bọc quanh deque
class TypedQueue[T]:
    def __init__(self) -> None:
        self._items: deque[T] = deque()

    def enqueue(self, item: T) -> None:
        self._items.append(item)

    def dequeue(self) -> T:
        if not self._items:
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def peek(self) -> T:
        if not self._items:
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)


# Chạy thử nghiệm
if __name__ == "__main__":
    stack: TypedStack[int] = TypedStack()
    stack.push(10)
    stack.push(20)
    print("TypedStack peek:", stack.peek()) # 20
    print("TypedStack pop:", stack.pop())   # 20

    queue: TypedQueue[str] = TypedQueue()
    queue.enqueue("Task 1")
    queue.enqueue("Task 2")
    print("TypedQueue peek:", queue.peek())      # Task 1
    print("TypedQueue dequeue:", queue.dequeue())# Task 1
