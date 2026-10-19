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
# Ví dụ chạy bài học về biến & số học:
python "0. Python Basics/0. Data Types and Variables/0_variables_and_numbers.py"

# Ví dụ chạy thuật toán Dijkstra:
python "6. Algorithms/2. Graph and Tree Algorithms/Graphs/dijkstra.py"
```

---

## 📂 Cấu trúc chương mục (Curriculum Structure)

* **[0. Python Basics](./0.%20Python%20Basics)**:
  * `0. Data Types and Variables` *(Nhóm Biến & Kiểu dữ liệu nguyên thủy)*:
    * `0_variables_and_numbers.py`: Hàm xuất dữ liệu `print()`, khai báo biến, 4 kiểu dữ liệu cơ bản (`int`, `float`, `str`, `bool`), ép kiểu (`int()`, `float()`, `str()`), phép toán số học (`+`, `-`, `*`, `/`, `//`, `%`, `**`), toán tử gán kết hợp (`+=`), thứ tự ưu tiên ngoặc đơn `()` và làm tròn `round()`.
    * `1_strings.py`: Tạo chuỗi, Indexing, Slicing, định dạng f-strings, và các phương thức xử lý chuỗi cốt lõi (`upper`, `lower`, `strip`, `replace`, `split`, toán tử `in`, tính bất biến).
  * `1. Control Flow` *(Nhóm Điều khiển luồng)*:
    * `2_conditionals.py`: Toán tử so sánh, toán tử thành viên `in` / `not in`, hàm kiểm tra `bool()` & giá trị Falsy, câu lệnh `if`, cấu trúc `if - elif - else`, Nested if, logic `and`/`or`/`not`, toán tử 3 ngôi (Ternary), và so khớp mẫu `match - case` (Python 3.10+).
    * `3_loops.py`: Vòng lặp `for` với danh sách và chuỗi, tham số `range()` (`start`, `stop`, `step`), vòng lặp `while`, câu lệnh điều khiển `break`, `continue`, và vòng lặp lồng nhau (`nested loop`).
  * `2. Functions and Modules` *(Nhóm Hàm & Tổ chức mô-đun)*:
    * `4_functions.py`: Định nghĩa hàm `def`, placeholder `pass`, giá trị trả về `return`, tham số mặc định, keyword arguments, đối số linh hoạt `*args` và `**kwargs`, phạm vi biến Local vs Global (`global`).
    * `5_modules.py`: Cú pháp `import`, trích xuất `from ... import`, đặt bí danh `as`, thư viện chuẩn `math` (`sqrt`, `floor`, `ceil`, `pow`) và `random` (`random`, `randint`, `uniform`, `choice`, `choices`, `sample`), thư viện bên ngoài qua `pip` (`numpy`), và idiom `if __name__ == '__main__':`.
    * `6_datetime.py`: Xử lý ngày tháng và thời gian với module `datetime` (`date`, `datetime`), phép toán thời gian (`timedelta`), truy xuất thuộc tính (`year`, `month`, `day`, `hour`, `minute`, `second`), phương thức bất biến `replace()`, định dạng chuỗi `strftime()`, và múi giờ UTC hiện đại `timezone.utc` (Python 3.12+).
* **[1. Collections](./1.%20Collections)**:
  * `0. Sequences`:
    * `lists_and_tuples.py`: List và Tuple: Chỉ mục, cắt lát (`slicing`), gán lát cắt, giải nén (`*rest`), các phương thức list (`append`, `insert`, `extend`, `remove`, `pop`, `del`, `sort`, `copy`, `index`, `count`), tính bất biến của tuple.
  * `1. Sets`:
    * `sets.py`: Tập hợp không thứ tự và không trùng lặp, thêm/xóa (`add`, `update`, `remove`, `discard`, `pop`), tra cứu `in` $O(1)$, đại số tập hợp (`|`, `&`, `-`, `^`), tập con `<=`, tập hợp bất biến `frozenset`, lọc trùng trong list.
  * `2. Dictionaries`:
    * `dictionaries.py`: Cặp khóa - giá trị, truy cập an toàn `.get()`, thêm/sửa, gộp từ điển (`|`), view objects (`keys`, `values`, `items`), xóa (`pop`, `popitem`, `del`), sao chép `.copy()`, dictionary lồng nhau, đếm tần suất.
  * `3. Iteration and Comprehensions`:
    * `advanced_iteration.py`: Duyệt với `enumerate()`, ghép song song `zip()`, Iterator (`iter`, `next`), Generator (`yield`, `yield from`), `itertools` (`chain`, `islice`, `batched`).
    * `comprehensions_and_lambdas.py`: List Comprehension, toán tử Walrus (`:=`), làm phẳng ma trận 2D, Generator Expression, hàm ẩn danh `lambda`, sắp xếp theo key, hàm logic `all()` và `any()`.
  * `4. Specialized Containers`:
    * `collections_module.py`: Bộ đếm tần suất tự động `Counter`, từ điển có giá trị mặc định `defaultdict`, dữ liệu nhẹ có tên trường `namedtuple`, hàng đợi hai đầu `deque` và cửa sổ trượt `maxlen`.
* **[2. Error Handling & File I/O](./2.%20Error%20Handling)**:
  * `0_exceptions.py`: Xử lý ngoại lệ (`try - except - else - finally`), ném ngoại lệ (`raise`), Custom Exception, `ExceptionGroup` & `except*`, ghi log chuyên nghiệp với `logging` và trích xuất Traceback.
  * `1_file_handling.py`: Thao tác tệp tin cổ điển với `open()`, Context Manager `with`, và quản lý tệp hiện đại với `pathlib.Path` (`write_text`, `read_text`, `unlink`).
  * `2_json_and_csv.py`: Xử lý tệp dữ liệu có cấu trúc: JSON (`loads`, `dumps`, `load`, `dump`) và bảng tính CSV (`reader`, `writer`, `DictReader`, `DictWriter`).
* **[3. OOP and Classes](./3.%20OOP%20and%20Classes)**:
  * 6 bài học cốt lõi tuần tự: `0_classes_and_objects.py` (Lớp, Đối tượng, Khởi tạo `__init__`, `self`, `__str__`, Biến Class vs Instance, `@classmethod`, `@staticmethod`) $\rightarrow$ `1_encapsulation.py` (Đóng gói Encapsulation, thuộc tính Private `__`, Getter/Setter và `@property`) $\rightarrow$ `2_inheritance.py` (Kế thừa đơn, ghi đè Overriding, `super()`, Đa kế thừa & MRO, Composition) $\rightarrow$ `3_polymorphism.py` (Đa hình) $\rightarrow$ `4_abstraction.py` (Trừu tượng ABC & Protocol) $\rightarrow$ `5_special_methods.py` (Dunder methods).
* **[4. Complexity and Recursion](./4.%20Complexity%20and%20Recursion)**:
  * 3 bài học nền tảng: `0_big_o.py` (Phân tích Big O) $\rightarrow$ `1_recursion_basics.py` (Nền tảng đệ quy & Call Stack) $\rightarrow$ `2_problem_solving.py` (Kỹ thuật giải bài toán: Two Pointers, Sliding Window).
* **[5. Data Structures](./5.%20Data%20Structures)**:
  * `0. Linear Structures` *(Cấu trúc tuyến tính)*:
    * `Arrays and Buffers`: `arrays.py` (Mảng tĩnh vs Mảng động, cơ chế Doubling, so sánh tiêu tốn bộ nhớ với `array.array`, và bộ đệm nhị phân C `bytearray`).
    * `Linked Lists`: `linked_lists.py` (Danh sách liên kết đơn Singly Linked List).
    * `Stacks`: `stacks.py` (Ngăn xếp LIFO, cài bằng mảng và Type-Safe Generic `Stack[T]` chuẩn Python 3.12+).
    * `Queues`: `queues.py` (Hàng đợi FIFO, cài bằng deque O(1) và Type-Safe Generic `Queue[T]` chuẩn Production).
  * `1. Hash-based Structures` *(Cấu trúc băm)*:
    * `custom_hash_table.py`: Cài đặt Bảng băm từ đầu với Chaining giải quyết xung đột & Lý thuyết Map ADT vs Hash Table.
  * `2. Non-linear Structures` *(Cấu trúc phi tuyến tính)*:
    * `Graphs`: Đồ thị tổng quát (`graphs.py`).
    * `Trees`: Họ hàng nhà cây (`trees_and_bst.py`, `heaps.py`, `tries.py`).
* **[6. Algorithms](./6.%20Algorithms)**:
  * `0. Searching`: `linear_search.py` (Tìm kiếm tuyến tính), `binary_search.py` (Tìm kiếm nhị phân).
  * `1. Sorting Algorithms`: Các thuật toán sắp xếp kinh điển: `heap_sort.py`, `merge_sort.py`, `quick_sort.py`, `timsort_hybrid.py` (thuật toán lai chuẩn của Python).
  * `2. Graph and Tree Algorithms`:
    * `Graphs`: Thuật toán đồ thị: `bfs_dfs.py` (BFS/DFS trên đồ thị), `dijkstra.py` (Đường đi ngắn nhất), `n_queens.py` (Quay lui Backtracking), `topological_sort.py` (Sắp xếp Topo & Phát hiện chu trình DAG bằng Kahn BFS và 3-Color DFS), `minimum_spanning_tree.py` (Cây khung nhỏ nhất MST với Kruskal & DSU và Prim Min-Heap).
    * `Trees`: Duyệt cây nhị phân: `tree_traversals.py` (BFS Level-order, DFS Pre/In/Post-order).
  * `3. Dynamic Programming`: `fibonacci.py` (Lý thuyết cốt lõi DP, 4 cấp độ tối ưu Fibonacci & Bài toán Climbing Stairs), `coin_change.py` (Đổi xu tối ưu), `knapsack_01.py` (Bài toán Cái túi 0/1, bảng 2D, truy vết và tối ưu 1D), `longest_common_subsequence.py` (Chuỗi con chung dài nhất LCS và Dãy con tăng dài nhất LIS $O(n \log n)$).
* **[7. Concurrency and Async](./7.%20Concurrency%20and%20Async)**:
  * `0_threading.py`: Đa luồng (Threading), tác vụ I/O-bound, bẫy tranh chấp dữ liệu (Race condition), khóa đồng bộ `threading.Lock`, và quản lý bể luồng với `ThreadPoolExecutor`.
  * `1_multiprocessing.py`: Đa tiến trình (Multiprocessing), tác vụ CPU-bound, vượt qua rào cản GIL, cơ chế `spawn` trên Windows, và tăng tốc đa nhân với `ProcessPoolExecutor`.
  * `2_asyncio_basics.py`: Lập trình bất đồng bộ đơn luồng (AsyncIO), Coroutines (`async/await`), Event Loop, chạy đồng thời `asyncio.gather()`, cấu trúc hiện đại `asyncio.TaskGroup()` (Python 3.11+), so sánh Non-blocking vs Blocking.

---

## 🌳 Bản đồ Quan hệ Phân cấp Cha - Con & Anh Em (Concepts Hierarchy)

### 🧬 Cây Gia Phả Hệ Thống Kiểu Dữ Liệu Python (Độc quyền các kiểu trong dự án)

```text
object (Tổ tiên chung tối cao)
 │
 ├── 🔢 NHÓM SỐ HỌC (Numeric Types - Đều là Hashable [#])
 │    ├── int (Số nguyên)
 │    │    └── bool (True / False - Lớp con trực tiếp của int)
 │    ├── float (Số thực)
 │    └── complex (Số phức)
 │
 ├── 📦 NHÓM TẬP HỢP (collections.abc.Collection)
 │    ├── Sequence (Chuỗi tuần tự có thứ tự & chỉ mục)
 │    │    ├── [Bất biến / Hashable #]: str, tuple, range, bytes
 │    │    └── [Khả biến / Unhashable]: list, bytearray
 │    │
 │    ├── Set (Tập hợp các phần tử duy nhất)
 │    │    ├── [Bất biến / Hashable #]: frozenset
 │    │    └── [Khả biến / Unhashable]: set
 │    │
 │    └── Mapping (Ánh xạ Khóa - Giá trị)
 │         └── [Khả biến / Unhashable]: dict (Chỉ nhận Key là Hashable [#])
 │
 └── 🧩 NHÁNH ĐẶC BIỆT & THỰC THI (Special & Callable)
      ├── NoneType (Chỉ chứa giá trị duy nhất: None)
      └── Callable (Có thể gọi với `()`): function, lambda, generator, class, method
```

### 📋 Bảng Tra Cứu Phân Cấp Chi Tiết (Sắp xếp theo Lộ trình 0 → 7)

| Chương | Khái niệm Cha (Parent) | Khái niệm Con (Child / Subtype) | Khái niệm Cháu (Specialization) | Bản chất quan hệ | Thư mục & Tệp mã nguồn |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **0** | **int** (Số nguyên) | **bool** (Boolean) | True / False | `bool` là lớp con trực tiếp của `int` | `0. Python Basics/0. Data Types and Variables/0_variables_and_numbers.py` |
| **0** | **Sequence** | str (Chuỗi ký tự) | Slicing & f-strings | Chuỗi bất biến (Immutable Sequence) | `0. Python Basics/0. Data Types and Variables/1_strings.py` |
| **0** | **Control Flow** | Conditionals & Loops | for vs while, if vs match | Hai nhánh anh em điều khiển luồng thực thi | `0. Python Basics/1. Control Flow/` |
| **0** | **Scope** | Local vs Global | *args, **kwargs, default args | Định nghĩa hàm và phạm vi biến | `0. Python Basics/2. Functions and Modules/4_functions.py` |
| **0** | **Module System** | import, math, random | Third-party packages (numpy) | Tái sử dụng và mở rộng chức năng | `0. Python Basics/2. Functions and Modules/5_modules.py` |
| **0** | **Time Handling** | date, datetime | timedelta, timezone.utc | Xử lý thời gian và múi giờ hiện đại (Python 3.12+) | `0. Python Basics/2. Functions and Modules/6_datetime.py` |
| **1** | **Sequence** | list & tuple | Slicing, unpack, list methods | Cặp sinh đôi Sequence (`list` khả biến & `tuple` bất biến) | `1. Collections/0. Sequences/lists_and_tuples.py` |
| **1** | **Set** (Tập hợp) | set (Khả biến) & frozenset (Bất biến) | — | Hai anh em ruột: `set` vs `frozenset` (bất biến & băm được) | `1. Collections/1. Sets/sets.py` |
| **1** | **Mapping** | **dict** (Dictionary) | dict union (`\|`), view objects | Nhánh ánh xạ Key-Value (anh em họ với Set) | `1. Collections/2. Dictionaries/dictionaries.py` |
| **1** | **Iteration** | List Comprehension | Walrus `:=`, Generator, Lambda | Kỹ thuật lặp và tối ưu biểu thức | `1. Collections/3. Iteration and Comprehensions/comprehensions_and_lambdas.py` |
| **1** | **Stream Iteration** | Iterator & Generator | yield, itertools.batched | Luồng lặp lười (Lazy Evaluation) | `1. Collections/3. Iteration and Comprehensions/advanced_iteration.py` |
| **1** | **Container** | dict & tuple mở rộng | Counter, defaultdict, deque | Cấu trúc chuyên biệt đếm tần suất và hàng đợi 2 đầu | `1. Collections/4. Specialized Containers/collections_module.py` |
| **2** | **Exception** | try - except - else - finally | ExceptionGroup, logging, traceback | Xử lý lỗi toàn diện và ghi nhật ký ứng dụng | `2. Error Handling/0_exceptions.py` |
| **2** | **File I/O** | open() & with | pathlib.Path | Quản lý tệp tin truyền thống và hướng đối tượng | `2. Error Handling/1_file_handling.py` |
| **2** | **Data Formats** | Serialization | JSON & CSV | Đọc/ghi dữ liệu cấu trúc lồng nhau và bảng tính | `2. Error Handling/2_json_and_csv.py` |
| **3** | **OOP Pillar** | Class & Object | __init__, self, __str__ | Lớp, đối tượng và phương thức đặc biệt | `3. OOP and Classes/0_classes_and_objects.py` |
| **3** | **OOP Pillar** | Encapsulation | Private `__`, Getter/Setter, @property | Che giấu trạng thái và kiểm soát truy cập thuộc tính | `3. OOP and Classes/1_encapsulation.py` |
| **3** | **OOP Pillar** | Inheritance | Method Overriding, super(), MRO | Kế thừa đơn, đa kế thừa và phân giải phương thức | `3. OOP and Classes/2_inheritance.py` |
| **3** | **OOP Pillar** | Polymorphism | Duck Typing vs Inheritance Polymorphism | Đa hình linh hoạt không ràng buộc và kế thừa | `3. OOP and Classes/3_polymorphism.py` |
| **3** | **OOP Pillar** | Abstraction | ABC (@abstractmethod) & Protocol | Lớp trừu tượng danh nghĩa và Duck Typing tĩnh | `3. OOP and Classes/4_abstraction.py` |
| **3** | **OOP Pillar** | Dunder Methods | __len__, __getitem__, __add__... | Nạp chồng toán tử và biến đối tượng thành Container | `3. OOP and Classes/5_special_methods.py` |
| **4** | **Complexity** | Big O Analysis | O(1), O(log n), O(n), O(n^2)... | Đo lường độ phức tạp thời gian và không gian | `4. Complexity and Recursion/0_big_o.py` |
| **4** | **Recursion** | Call Stack | Base case & Recursive step | Kỹ thuật chia để trị nền tảng | `4. Complexity and Recursion/1_recursion_basics.py` |
| **4** | **Problem Solving** | Two Pointers | Sliding Window | Hai kỹ thuật vàng giải bài toán mảng/chuỗi | `4. Complexity and Recursion/2_problem_solving.py` |
| **5** | **Linear DS** | Arrays & Buffers | list vs array.array vs bytearray | Mảng liên tục và bộ đệm nhị phân | `5. Data Structures/0. Linear Structures/Arrays and Buffers/arrays.py` |
| **5** | **Linear DS** | Singly Linked List | Node traversal & modification | Danh sách liên kết đơn cấp phát động | `5. Data Structures/0. Linear Structures/Linked Lists/linked_lists.py` |
| **5** | **Linear DS** | Stack & Queue | LIFO vs FIFO, collections.deque | Ngăn xếp và hàng đợi chuẩn Type-Safe [T] | `5. Data Structures/0. Linear Structures/Stacks/` & `Queues/` |
| **5** | **Hash Map** | Map ADT vs Hash Table | Separate Chaining | Bảng băm tự thiết kế giải quyết xung đột | `5. Data Structures/1. Hash-based Structures/custom_hash_table.py` |
| **5** | **Non-linear DS** | Graphs & Trees | Adjacency List, BST, Binary Heap | Đồ thị tổng quát, cây tìm kiếm và Heap ưu tiên | `5. Data Structures/2. Non-linear Structures/` |
| **6** | **Search** | Linear Search | Binary Search | Tìm kiếm tuyến tính và nhị phân | `6. Algorithms/0. Searching/` |
| **6** | **Sorting** | Divide & Conquer | Merge Sort, Quick Sort, Timsort | Các thuật toán sắp xếp kinh điển chuẩn công nghiệp | `6. Algorithms/1. Sorting Algorithms/` |
| **6** | **Graph & Tree** | BFS & DFS | Dijkstra, Topological Sort, MST | Duyệt cây, đường đi ngắn nhất, sắp xếp topo | `6. Algorithms/2. Graph and Tree Algorithms/` |
| **6** | **Dynamic Programming** | Memoization & Tabulation | Fibonacci, Coin Change, Knapsack, LCS | Quy hoạch động từ bài toán con đến tối ưu mảng 1D | `6. Algorithms/3. Dynamic Programming/` |
| **7** | **Concurrency** | I/O-Bound vs Preemption | Threading & Lock | Đa luồng chia sẻ bộ nhớ và ngăn ngừa Race condition | `7. Concurrency and Async/0_threading.py` |
| **7** | **Parallelism** | CPU-Bound vs Multi-Core | Multiprocessing | Đa tiến trình vượt rào cản GIL tận dụng đa nhân CPU | `7. Concurrency and Async/1_multiprocessing.py` |
| **7** | **Asynchronous I/O** | Single-Thread Event Loop | Coroutine, TaskGroup (Python 3.11+) | Bất đồng bộ non-blocking với hàng ngàn kết nối đồng thời | `7. Concurrency and Async/2_asyncio_basics.py` |




