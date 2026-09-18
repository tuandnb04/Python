from abc import ABC, abstractmethod
import random


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


if __name__ == '__main__':
    pawn = Pawn()
    print("Initial position:", pawn.position)
    print("Move 1:", pawn.make_move())
    print("Move 2:", pawn.make_move())
    
    # Nâng cấp người chơi: mở rộng thêm các bước đi chéo
    pawn.level_up()
    print("Move after level up:", pawn.make_move())
    print("Total path:", pawn.path)