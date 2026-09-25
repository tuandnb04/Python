# Custom Linked Lists (Danh sách liên kết tự cài đặt bằng Node con trỏ)
# - Ghi chú: Thường dùng trong phỏng vấn thuật toán (LeetCode) hoặc cấu trúc dữ liệu kinh điển.
# - Trong thực tế dự án Python, ưu tiên dùng 'collections.deque' hoặc 'list' có sẵn với hiệu năng C vượt trội.

from __future__ import annotations

# 1. Singly Linked List (Danh sách liên kết đơn: duyệt 1 chiều)
class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None  # Tham chiếu tới node tiếp theo

class SinglyLinkedList:
    def __init__(self):
        self.head: Node | None = None

    # Chèn vào đầu danh sách: O(1) - Constant Time
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Chèn vào cuối danh sách: O(n) - Phải duyệt qua n node
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    # Xóa ở đầu: O(1)
    def remove_from_beginning(self):
        if not self.head:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data

    # Xóa ở cuối: O(n)
    def remove_from_end(self):
        if not self.head:
            return None
        if not self.head.next:
            removed_data = self.head.data
            self.head = None
            return removed_data

        curr = self.head
        while curr.next and curr.next.next:
            curr = curr.next

        last_node = curr.next
        if last_node is None:
            return None

        removed_data = last_node.data
        curr.next = None
        return removed_data

    # Chèn vào sau một giá trị mục tiêu (ở giữa): O(n) tìm kiếm, O(1) chèn
    def insert_after(self, target_data, new_data):
        curr = self.head
        while curr and curr.data != target_data:
            curr = curr.next
        if curr:
            new_node = Node(new_data)
            new_node.next = curr.next
            curr.next = new_node

    # Xóa một node theo giá trị: O(n)
    def remove_node(self, target_data):
        if not self.head:
            return False
        if self.head.data == target_data:
            self.head = self.head.next
            return True

        curr = self.head
        while curr.next and curr.next.data != target_data:
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next
            return True
        return False

    def display(self):
        res, curr = [], self.head
        while curr:
            res.append(curr.data)
            curr = curr.next
        return " -> ".join(map(str, res)) if res else "Empty"

sll = SinglyLinkedList()
sll.insert_at_beginning("B")
sll.insert_at_beginning("A")       # O(1) -> A -> B
sll.insert_at_end("D")             # O(n) -> A -> B -> D
sll.insert_after("B", "C")         # O(n) -> A -> B -> C -> D
print("Singly Linked List:", sll.display()) # A -> B -> C -> D

sll.remove_node("B")
print("After removing 'B':", sll.display())  # A -> C -> D
sll.remove_from_end()
print("After removing end:", sll.display())  # A -> C


# 2. Doubly Linked List (Danh sách liên kết đôi: duyệt 2 chiều)
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev: DoublyNode | None = None  # Tham chiếu về node trước
        self.next: DoublyNode | None = None  # Tham chiếu tới node sau (tốn bộ nhớ hơn Singly)

class DoublyLinkedList:
    def __init__(self):
        self.head: DoublyNode | None = None
        self.tail: DoublyNode | None = None

    # Chèn đầu: O(1)
    def insert_at_beginning(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Chèn cuối: O(1) nhờ có con trỏ tail
    def insert_at_end(self, data):
        new_node = DoublyNode(data)
        if not self.tail:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    # Xóa đầu: O(1)
    def remove_from_beginning(self):
        if not self.head:
            return None
        removed_data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
        return removed_data

    # Xóa cuối: O(1) nhờ có con trỏ tail và prev
    def remove_from_end(self):
        if not self.tail:
            return None
        removed_data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            if self.tail is not None:
                self.tail.next = None
        return removed_data

    def display_forward(self):
        res, curr = [], self.head
        while curr:
            res.append(curr.data)
            curr = curr.next
        return " <-> ".join(map(str, res)) if res else "Empty"

    def display_backward(self):
        res, curr = [], self.tail
        while curr:
            res.append(curr.data)
            curr = curr.prev
        return " <-> ".join(map(str, res)) if res else "Empty"

dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_beginning(0)

print("\nDoubly Forward :", dll.display_forward())   # 0 <-> 10 <-> 20 <-> 30
print("Doubly Backward:", dll.display_backward())  # 30 <-> 20 <-> 10 <-> 0

dll.remove_from_end()
print("After remove end:", dll.display_forward())   # 0 <-> 10 <-> 20

