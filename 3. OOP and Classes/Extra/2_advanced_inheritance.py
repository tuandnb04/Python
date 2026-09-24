# ADVANCED INHERITANCE: DEEP MRO & COOPERATIVE MULTIPLE INHERITANCE
#
# Kiến thức nâng cao về cơ chế giải quyết thứ tự phương thức (Method Resolution Order - MRO)
# và cách thức hoạt động thực sự của `super()` trong đa kế thừa phức tạp (Cooperative Multiple Inheritance).

# QUAN TRỌNG: `super()` trong Python KHÔNG đơn thuần là "gọi lớp cha trực tiếp".
# `super()` có nghĩa là: "Gọi class TIẾP THEO trong chuỗi MRO (Next in MRO)".
# Khi các lớp phối hợp gọi `super()`, Python duyệt qua chuỗi MRO theo thuật toán C3 Linearization.

class Base:
    def action(self) -> None:
        print("Base action")

class Step1(Base):
    def action(self) -> None:
        print("Step1 action (before)")
        super().action()
        print("Step1 action (after)")

class Step2(Base):
    def action(self) -> None:
        print("Step2 action (before)")
        super().action()
        print("Step2 action (after)")

class Combined(Step1, Step2):
    def action(self) -> None:
        print("Combined action (start)")
        super().action()
        print("Combined action (end)")


print("MRO of Combined:", [cls.__name__ for cls in Combined.mro()])
# Thứ tự MRO: Combined -> Step1 -> Step2 -> Base -> object
# Quá trình thực thi:
# 1. Combined.action() gọi super() -> nhảy sang Step1.action()
# 2. Step1.action() gọi super() -> nhảy sang Step2.action() (không phải Base!)
# 3. Step2.action() gọi super() -> nhảy sang Base.action()
# 4. Khi Base xong, luồng quay ngược lại hoàn tất các câu lệnh sau super() của Step2, rồi Step1, rồi Combined.

c = Combined()
c.action()


# Python sử dụng thuật toán C3 Linearization để tính thứ tự MRO:
# 1. Con luôn xuất hiện trước Cha.
# 2. Thứ tự các lớp cha trong khai báo tuple kế thừa được bảo toàn (từ trái qua phải).
# 3. Nếu không tìm được thứ tự thỏa mãn tính nhất quán, Python sẽ chặn khởi tạo và ném lỗi `TypeError`.

class X:
    pass

class Y:
    pass

class A(X, Y):
    pass

class B(Y, X):
    pass

# Thử nghiệm tạo class xung đột thứ tự sẽ gây TypeError:
try:
    type("Bad", (A, B), {})
except TypeError as e:
    print("Cannot create class due to MRO conflict:", e)
