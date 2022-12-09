#!/usr/bin/env python
""" AoC 2022 Day 9"""
from copy import deepcopy


class Snake:
    """Process the signals"""

    def __init__(self, length: int) -> None:
        self.instr_list: list = []
        self.visited_locations: dict[tuple, int] = {(0, 0): 1}
        self.snake: list = []
        self.old_snake: list = []

        for _ in range(length):
            self.snake.append([0, 0])

    def load_game(self, file_name: str) -> None:
        """Load the game from the input"""

        with open(file_name, encoding="UTF-8") as in_file:
            self.instr_list = [instr.split(" ") for instr in in_file.read().split("\n")]

    def adjust_snake(self, first: int, second: int) -> None:
        """Check for the tail pos and adjust it"""

        # same or adjacent

        if (
            abs(self.snake[first][0] - self.snake[second][0]) <= 1
            and abs(self.snake[first][1] - self.snake[second][1]) <= 1
        ):

            return

        if self.snake[first][0] - self.snake[second][0] > 1:
            self.old_snake[second][0] += 1

            if self.snake[first][1] - self.snake[second][1] > 0:
                self.old_snake[second][1] += 1

            if self.snake[first][1] - self.snake[second][1] < 0:
                self.old_snake[second][1] -= 1
            return

        if self.snake[first][0] - self.snake[second][0] < -1:
            self.old_snake[second][0] -= 1
            if self.snake[first][1] - self.snake[second][1] > 0:
                self.old_snake[second][1] += 1

            if self.snake[first][1] - self.snake[second][1] < 0:
                self.old_snake[second][1] -= 1
            return

        if self.snake[first][1] - self.snake[second][1] > 1:
            self.old_snake[second][1] += 1
            if self.snake[first][0] - self.snake[second][0] > 0:
                self.old_snake[second][0] += 1

            if self.snake[first][0] - self.snake[second][0] < 0:
                self.old_snake[second][0] -= 1
            return

        if self.snake[first][1] - self.snake[second][1] < -1:
            self.old_snake[second][1] -= 1
            if self.snake[first][0] - self.snake[second][0] > 0:
                self.old_snake[second][0] += 1

            if self.snake[first][0] - self.snake[second][0] < 0:
                self.old_snake[second][0] -= 1

    def part1(self) -> int:
        """Get the first part result"""

        moves: dict = {"R": (0, 1), "U": (-1, 0), "L": (0, -1), "D": (1, 0)}
        for instr in self.instr_list:

            try:
                for _ in range(int(instr[1])):
                    self.snake[0][0] += moves[instr[0]][0]
                    self.snake[0][1] += moves[instr[0]][1]

                    for part in range(len(self.snake) - 1):
                        self.old_snake = deepcopy(self.snake)
                        self.adjust_snake(first=part, second=part + 1)
                        self.snake = deepcopy(self.old_snake)
                    self.visited_locations[tuple(self.snake[-1])] = 1

            except IndexError:
                pass

        return len(self.visited_locations.keys())

    def part2(self) -> int:
        """Get the second part result"""


def main() -> None:
    """Do the tasks"""
    game = Snake(length=2)
    game.load_game(file_name="input9.txt")
    print(game.part1())
    game = Snake(length=10)
    game.load_game(file_name="input9.txt")
    print(game.part1())


if __name__ == "__main__":
    main()


def test_part1() -> None:
    """Tester for part 1"""
    test_game = Snake(length=2)
    test_game.load_game(file_name="input9_test.txt")
    assert test_game.part1() == 13


def test_part2() -> None:
    """Tester for part 2"""
    test_game = Snake(length=10)
    test_game.load_game(file_name="input9_test.txt")

    test_game.part1()
    assert test_game.part1() == 1
