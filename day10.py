#!/usr/bin/env python
""" AoC 2022 Day 10"""
import numpy as np


class CPU:
    """Process the signals"""

    inst_len: dict = {"noop": 1, "addx": 2}

    def __init__(self) -> None:
        self.instr_list: list = []
        self.register: dict = {"X": 1}
        self.cycle = 0
        self.crt: np.ndarray

    def load_game(self, file_name: str) -> None:
        """Load the game from the input"""

        with open(file_name, encoding="UTF-8") as in_file:
            self.instr_list = [instr.split(" ") for instr in in_file.read().split("\n")]

    def print_grid(self) -> None:
        """Print the grid"""

        for x in range(0, 6):
            for y in range(0, 40):
                if self.crt[x][y]:
                    print("█", end="")
                else:
                    print(" ", end="")

            print("")

    def part1(self) -> int:
        """Get the first part result"""

        self.crt = np.zeros(40 * 6, dtype=str).reshape(6, 40)
        result_sum = 0

        for instr in self.instr_list:

            try:
                for _ in range(self.inst_len[instr[0]]):
                    self.cycle += 1
                    if self.cycle == 20 or (self.cycle - 20) % 40 == 0:
                        result_sum += int(self.register["X"]) * self.cycle

                    row, pos = divmod(self.cycle - 1, 40)
                    if pos in range(self.register["X"] - 1, self.register["X"] + 2):
                        self.crt[row, pos] = "X"

                if instr[0] == "addx":
                    self.register["X"] += int(instr[1])
            except KeyError:
                pass

        self.print_grid()
        return result_sum

    def part2(self) -> int:
        """Get the second part result"""


def main() -> None:
    """Do the tasks"""
    game = CPU()
    game.load_game(file_name="input10.txt")
    print(game.part1())


if __name__ == "__main__":
    main()


def test_part1() -> None:
    """Tester for part 1"""
    test_game = CPU()
    test_game.load_game(file_name="input10_test.txt")
    assert test_game.part1() == 13140
