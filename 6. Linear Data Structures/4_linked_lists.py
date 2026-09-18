# Node của Singly Linked List (Danh sách liên kết đơn: duyệt 1 chiều)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None          # Tham chiếu tới node tiếp theo

class SinglyLinkedList:
    def __init__(self):
        self.head = None

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
        if self.head:
            self.head = self.head.next

    def display(self):
        res, curr = [], self.head
        while curr:
            res.append(curr.data)
            curr = curr.next
        return " -> ".join(map(str, res))

sll = SinglyLinkedList()
sll.insert_at_beginning("B")
sll.insert_at_beginning("A")       # O(1)
sll.insert_at_end("C")             # O(n)
print("Singly Linked List:", sll.display()) # A -> B -> C

# Node của Doubly Linked List (Danh sách liên kết đôi: duyệt 2 chiều)
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None           # Tham chiếu về node trước
        self.next = None           # Tham chiếu tới node sau (tốn bộ nhớ hơn Singly)
