# Python Projects & Learning Roadmap

Kho tài liệu và mã nguồn học tập Python từ cơ bản đến nâng cao, bao gồm cú pháp cốt lõi, lập trình hướng đối tượng (OOP), cấu trúc dữ liệu và giải thuật.

---

## 🚀 Khởi động nhanh (Getting Started)

### 1. Kiểm tra phiên bản Python
Mở Terminal / PowerShell hoặc CMD và chạy lệnh:

```bash
# Trên Windows:
python --version
# hoặc:
py --version

# Trên macOS / Linux:
python3 --version
```

### 2. Sử dụng Python REPL (Interactive Shell)
Dùng để thử nghiệm các đoạn mã ngắn trực tiếp trên dòng lệnh:

```bash
# Mở trình thông dịch tương tác:
python
```
Dấu nhắc `>>>` sẽ xuất hiện. Bạn có thể gõ lệnh và xem kết quả ngay:
```python
>>> print("Hello, World!")
Hello, World!
>>> 1 + 1
2
```
Thoát khỏi REPL bằng cách gõ:
```python
>>> exit()
```

### 3. Thực thi một file script (`.py`)
Điều hướng đến thư mục dự án và chạy tệp bằng lệnh `python`:

```bash
# Ví dụ chạy bài học về biến:
python "0. Python Basics/1. Variables/variables.py"

# Ví dụ chạy thuật toán Dijkstra:
python "6. Algorithms/3. Graph and Tree Traversals/3_dijkstra.py"
```

---

## 📂 Cấu trúc chương mục (Curriculum Structure)

* **[0. Python Basics](file:///c:/Users/ASUS/Desktop/python-projects/0.%20Python%20Basics)**:
  * `1. Variables`: Khai báo biến, toán tử gán (`=`, `+=`, ...), toán tử Walrus (`:=`), kiểu dữ liệu, `print()`, `input()`, câu lệnh, PEP 8, hằng số, từ khóa `keyword`.
  * `2. Numbers`: Phép toán số học, toán tử gán kết hợp, toán tử Bitwise, thứ tự ưu tiên toán tử (`Operator Precedence`), chia nguyên/dư, math built-ins.
  * `3. Strings`: Cắt lát (slicing), chuỗi định dạng (f-strings), phương thức xử lý chuỗi.
  * `4. Conditionals`: Các toán tử điều kiện (logic, so sánh & `chaining`, danh tính `is`/`is not`, thành viên `in`/`not in`), thụt lề (`Indentation`), `if - elif - else`, toán tử 3 ngôi, Walrus trong `if`, `match - case`.
  * `5. Loops`: Vòng lặp `while`, vòng lặp `for` với `range()`, duyệt chuỗi `str`, điều khiển `break`, `continue`, `pass`, `for ... else`, `while ... else`, Walrus trong `while`.
  * `6. Functions`: Định nghĩa hàm, tham số, giá trị trả về, type hints, docstrings, generic `[T]`, `*args`, `**kwargs`, scope (`global`, `nonlocal`).
  * `7. Modules`: Thư viện chuẩn (`math`, `random`, `re`, `datetime`, `sys`), `StrEnum`.
* **[1. Collections and Sequences](file:///c:/Users/ASUS/Desktop/python-projects/1.%20Collections%20and%20Sequences)**:
  * `1. Lists`: Danh sách biến đổi (Mutable), 11 phương thức built-in, slicing & slice assignment, duyệt qua list, sắp xếp (`sort`), sao chép an toàn, nối list.
  * `2. Tuples`: Cấu trúc dữ liệu bất biến (Immutable), packing/unpacking, hoán đổi biến, pattern matching với tuple, phương thức `count()` và `index()`.
  * `3. Sets`: Tập hợp phần tử duy nhất, các phép toán tập hợp (hợp `|`, giao `&`, hiệu `-`, hiệu đối xứng `^`), kiểm tra tập con/tập cha, `frozenset`.
  * `4. Dictionaries`: Cặp Key - Value, truy cập an toàn với `.get()`, view objects (`keys`, `values`, `items`), hợp nhất dictionary (`|`, `|=`), cập nhật đệ quy.
  * `5. Advanced Iteration`: Kỹ thuật duyệt với `enumerate()`, ghép song song `zip()`, Iterator (`iter`, `next`), Generator (`yield`, `yield from`), `itertools` (`chain`, `islice`, `batched`), cửa sổ trượt `collections.deque`.
  * `6. Comprehensions and Lambdas`: Cú pháp rút gọn List/Dict/Set Comprehension, biểu thức điều kiện trong comp, Generator Expressions, hàm ẩn danh `lambda`, hàm bậc cao (`map`, `filter`, `all`, `any`, `sum`).
* **[2. Error Handling](file:///c:/Users/ASUS/Desktop/python-projects/2.%20Error%20Handling)**: Ngoại lệ (`try - except - finally`), Custom Exceptions, Debugging (`logging`, `pdb`, `breakpoint`), Thao tác tệp tin & File Handling (`open`, các chế độ `r/a/w/x/t/b`, đọc/ghi/nối/tạo file, `with` Context Manager, xóa file với `os.remove`).
* **[3. OOP and Classes](file:///c:/Users/ASUS/Desktop/python-projects/3.%20OOP%20and%20Classes)**: Class/Object, `@property`, kế thừa, đa hình, trừu tượng (ABC), Magic/Dunder methods (`__len__`, `__str__`, `__eq__`), thuộc tính động.
* **[4. Complexity and Recursion](file:///c:/Users/ASUS/Desktop/python-projects/4.%20Complexity%20and%20Recursion)**:
  * `Core`: Độ phức tạp thuật toán (Big O - Time & Space), Nền tảng đệ quy & Call Stack (LIFO), Kỹ thuật giải bài toán (Two Pointers, Edge cases).
  * `Extra`: Bài toán Tháp Hà Nội ($O(2^n)$), Đệ quy nâng cao (Accumulator, Deep Nested Sum, Recursion limit).
* **[5. Data Structures](file:///c:/Users/ASUS/Desktop/python-projects/5.%20Data%20Structures)**:
  * `Core`: Mảng động (Arrays / Lists - Time Complexity, Min Value), Ngăn xếp (Stacks - LIFO, Pancake analogy, Class Stack, Parentheses Matching), Hàng đợi (Queues - FIFO, `collections.deque`), Bảng băm & Tập hợp (Hash Maps & Sets), Heap (Priority Queue), Đồ thị (Graphs).
  * `Extra`: Danh sách liên kết (Singly & Doubly Linked Lists), Cài đặt Stack bằng Linked List (`LinkedListStack`), Cài đặt Queue bằng Linked List (`LinkedListQueue`), Generic Stack & Queue (`TypedStack`, `TypedQueue`), Bảng băm tự thiết kế (Custom Hash Table - 5 bước xây dựng từ đầu, Unicode Modulo, xử lý va chạm Chaining), Cây & Cây nhị phân (Trees & BST - Cấu trúc phân cấp, 4 loại cây nhị phân, BST Search/Insert/Delete), Cây AVL (AVL Trees - BST tự cân bằng, Balance Factor, 4 phép xoay LL/RR/LR/RL, Retracing, chứng minh $O(\log n)$), Cây tiền tố (Trie), Bộ đệm C tầng thấp (`bytearray`).
* **[6. Algorithms](file:///c:/Users/ASUS/Desktop/python-projects/6.%20Algorithms)**:
  * `1. Searching`: Tuyến tính (Linear Search - Toán tử `in`, quét tuần tự, tìm tất cả vị trí), Nhị phân (Binary Search - Mảng có thứ tự, duyệt chia đôi, lặp & đệ quy, xử lý phần tử trùng lặp, `bisect`).
  * `2. Sorting Algorithms`:
    * Thuật toán kinh điển (1-7): Sắp xếp nổi bọt (Bubble Sort - Cặp liền kề, tối ưu cờ `swapped` dừng sớm), Sắp xếp chọn (Selection Sort - Tìm min, Shifting Problem, tối ưu hoán đổi $O(1)$), Sắp xếp chèn (Insertion Sort - Mô phỏng xếp bài, In-place shifting, Binary Insertion Sort, Stable Sort), Sắp xếp nhanh (Quicksort - Chia để trị, Lomuto Partition, 3-Way Partition, Median-of-Three, $O(n \log n)$), Sắp xếp đếm phân phối (Counting Sort - Phi so sánh, $O(n + k)$, Stable Prefix Sum, xử lý số âm), Sắp xếp theo cơ số (Radix Sort - Phân loại theo chữ số LSD, 10 Buckets, vai trò của Stable Sort, CLRS Counting Subroutine, $O(n \cdot k)$), Sắp xếp trộn (Merge Sort - Chia để trị, đệ quy Top-down, không đệ quy Bottom-up, Stable Sort, $O(n \log n)$ mọi trường hợp).
    * `Extra`: Sắp xếp theo thùng (Bucket Sort - Phân tán số thực $[0, 1)$, sắp xếp cục bộ Insertion Sort, $O(n)$ trung bình), Thuật toán lai Timsort (Timsort Hybrid - Thuật toán mặc định của Python `list.sort()`, kết hợp Binary Insertion Sort và Merge Sort, $O(n)$ best case, $O(n \log n)$ worst case), Sắp xếp vun đống (Heap Sort - Dựa trên Max-Heap từ Chương 5, $O(n \log n)$ mọi trường hợp, $O(1)$ bộ nhớ phụ in-place).
  * `3. Graph and Tree Traversals`: Duyệt cây (BFS Level-order, DFS Pre/In/Post-order), BFS/DFS đồ thị, Dijkstra, N-Queens Backtracking.
  * `4. Dynamic Programming`: Leo bậc thang, Đổi tiền xu, LRU Cache, Fibonacci Memoization / Tabulation.
  * `5. Checksum and Math`: Thuật toán kiểm tra số thẻ Luhn.
