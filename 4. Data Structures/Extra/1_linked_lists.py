# Custom Linked Lists (Danh sách liên kết tự cài đặt bằng Node con trỏ)
# - Đặc tính: Cấu trúc dữ liệu tuyến tính kích thước động (dynamic), các node kết nối qua tham chiếu (reference).
# - Ứng dụng: Nền tảng xây dựng Stacks, Queues, Deques và danh sách kề trong duyệt đồ thị (BFS / DFS).
# - Chi phí bộ nhớ (Space): Mọi thao tác chèn / xóa đều đạt O(1) auxiliary space (không cần dịch chuyển mảng như Array).
# - Trong thực tế dự án Python, ưu tiên dùng 'collections.deque' hoặc 'list' có sẵn với hiệu năng C vượt trội.

from __future__ import annotations

# 1. Singly Linked List (Cài đặt dạng OOP Inner-Class: Node lồng bên trong LinkedList)
class LinkedList:
    class Node:
        def __init__(self, element):
            self.element = element
            self.next = None

    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def add(self, element):
        """Thêm phần tử vào cuối danh sách: O(n)"""
        node = self.Node(element)
        if self.is_empty():
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        self.length += 1

    def remove(self, element):
        """Xóa phần tử đầu tiên khớp giá trị: O(n)"""
        previous_node = None
        current_node = self.head
        while current_node is not None and current_node.element != element:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        elif previous_node is not None:
            previous_node.next = current_node.next
        else:
            self.head = current_node.next
        self.length -= 1

    def display(self):
        res, curr = [], self.head
        while curr:
            res.append(curr.element)
            curr = curr.next
        return " -> ".join(map(str, res)) if res else "Empty"


my_list = LinkedList()
print("my_list is_empty:", my_list.is_empty())

my_list.add(1)
my_list.add(2)
print("my_list is_empty:", my_list.is_empty())
print("my_list length:", my_list.length)
print("Elements:", my_list.display())

my_list.remove(1)
print("After removing 1:", my_list.display())
print("Length after remove:", my_list.length)


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

