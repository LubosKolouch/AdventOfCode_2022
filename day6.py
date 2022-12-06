#!/usr/bin/env python
""" AoC 2022 Day 6"""
from collections import Counter, deque


class SignalFinder:
    """Process the signals"""

    def __init__(self) -> None:
        self.message: str

    def load_game(self, file_name: str) -> None:
        """Load the game from the input"""

        with open(file_name, encoding="UTF-8") as in_file:
            message = in_file.readline()

        self.message = message

    def process_deque(self, maxlen: int) -> int:
        """Play each part"""
        signal_deque: deque = deque(maxlen=maxlen)

        for pos, item in enumerate(self.message):
            signal_deque.append(item)

            if (
                len(signal_deque) == maxlen
                and Counter(signal_deque).most_common(1)[0][1] == 1
            ):
                return pos + 1

        return 0

    def part1(self) -> int:
        """Get the first part result"""
        return self.process_deque(maxlen=4)

    def part2(self) -> int:
        """Get the second part result"""
        return self.process_deque(maxlen=14)


def main() -> None:
    """Do the tasks"""
    game = SignalFinder()
    game.load_game(file_name="input6.txt")
    print(game.part1())
    print(game.part2())


if __name__ == "__main__":
    main()


def test_part1() -> None:
    """Tester for part 1"""
    test_game = SignalFinder()
    test_game.load_game(file_name="input6_test.txt")
    assert test_game.part1() == 7


def test_part2() -> None:
    """Tester for part 2"""
    test_game = SignalFinder()
    test_game.load_game(file_name="input6_test.txt")
    assert test_game.part2() == 19
