from abc import ABC, abstractmethod
import random

# PHẦN 1: ABSTRACT CLASS CƠ BẢN (INTERFACE / CONTRACT CHUNG)
# Abstract class định nghĩa một "bản hợp đồng" (contract): mọi lớp con kế thừa
# BẮT BUỘC phải cài đặt (override) tất cả các phương thức có gắn @abstractmethod.

class PaymentGateway(ABC):  # Kế thừa từ Abstract Base Class (ABC)
    @abstractmethod
    def pay(self, amount: float) -> str:  # Lớp con bắt buộc phải override phương thức này
        pass


class CreditCardPayment(PaymentGateway):
    def pay(self, amount: float) -> str:
        return f"Processing credit card payment of ${amount:.2f}"


class PayPalPayment(PaymentGateway):
    def pay(self, amount: float) -> str:
        return f"Redirecting to PayPal for checkout: ${amount:.2f}"


class CryptoPayment(PaymentGateway):
    def pay(self, amount: float) -> str:
        return f"Broadcasting transaction to blockchain: ${amount:.2f}"


gateways: list[PaymentGateway] = [CreditCardPayment(), PayPalPayment(), CryptoPayment()]
for gateway in gateways:
    print(gateway.pay(49.99))

# Không thể khởi tạo trực tiếp instance từ abstract class:
# gateway = PaymentGateway() -> TypeError: Can't instantiate abstract class PaymentGateway with abstract method pay



# PHẦN 2: ABSTRACT CLASS CÓ __init__ VÀ THUỘC TÍNH DÙNG CHUNG

class TalkingToy(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def speak(self) -> None:
        pass


class RobotToy(TalkingToy):
    def speak(self) -> None:
        print(f'{self.name} says beep boop! I am a robot!')


class TeddyBearToy(TalkingToy):
    def speak(self) -> None:
        print(f"{self.name} says hug me! I'm cuddly!")


class DinosaurToy(TalkingToy):
    def speak(self) -> None:
        print(f'{self.name} says ROOOOAR!')


toys: list[TalkingToy] = [RobotToy('Rusty'), TeddyBearToy('Fluffy'), DinosaurToy('Rex')]
for toy in toys:
    toy.speak()


# PHẦN 3: ỨNG DỤNG THỰC TẾ: GAME PLAYER & ACTION INTERFACE

class Player(ABC):
    def __init__(self) -> None:
        self.moves: list[tuple[int, int]] = []
        self.position: tuple[int, int] = (0, 0)
        self.path: list[tuple[int, int]] = [self.position]

    def make_move(self) -> tuple[int, int]:
        move: tuple[int, int] = random.choice(self.moves)
        self.position = (self.position[0] + move[0], self.position[1] + move[1])
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self) -> None:
        pass


class Pawn(Player):
    def __init__(self) -> None:
        super().__init__()
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def level_up(self) -> None:
        self.moves.extend([(1, 1), (1, -1), (-1, 1), (-1, -1)])


pawn = Pawn()
print("Initial position:", pawn.position)
print("Move 1:", pawn.make_move())
print("Move 2:", pawn.make_move())

pawn.level_up()
print("Move after level up:", pawn.make_move())
print("Total path:", pawn.path)


# PHẦN 4: CHUẨN HIỆN ĐẠI (PYTHON 3.8+ / 3.12+): typing.Protocol (STRUCTURAL SUBTYPING)
# So sánh với ABC (Nominal Subtyping - phải kế thừa tường minh):
# - ABC: Bắt buộc class con phải kế thừa `class Dog(Animal)`.
# - Protocol: "Duck Typing" tĩnh - bất kỳ class nào có đủ phương thức đều tự động thỏa mãn interface mà KHÔNG CẦN kế thừa!

from typing import Protocol

class Renderable(Protocol):
    def render(self) -> str:
        """Bất kỳ class nào có phương thức render() -> str đều là Renderable."""
        ...

class Button:
    def render(self) -> str:
        return "[Submit Button]"

class Image:
    def render(self) -> str:
        return "<Image Asset>"

def display_ui(component: Renderable) -> None:
    print("Rendering component:", component.render())

# Button và Image không hề kế thừa Renderable nhưng vẫn hoàn toàn hợp lệ về Type Hint:
display_ui(Button())
display_ui(Image())

