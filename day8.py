#!/usr/bin/env python
""" AoC 2022 Day 8"""
import numpy as np


class TreeScout:
    """Process the signals"""

    def __init__(self) -> None:
        self.trees: np.ndarray
        self.visible_trees: dict = {}

    def load_game(self, file_name: str) -> None:
        """Load the game from the input"""

        with open(file_name, encoding="UTF-8") as in_file:
            self.trees = np.genfromtxt(file_name, delimiter=1, dtype=int)

    def part1(self) -> int:
        """Get the first part result"""

        for index, x in np.ndenumerate(self.trees):
            try:
                if x > max(self.trees[index[0], : index[1]]):
                    self.visible_trees[index] = x

                if x > max(self.trees[index[0], index[1] + 1 :]):
                    self.visible_trees[index] = x

                if x > max(self.trees[: index[0], index[1]]):
                    self.visible_trees[index] = x

                if x > max(self.trees[index[0] + 1 :, index[1]]):
                    self.visible_trees[index] = x

            except ValueError:
                self.visible_trees[index] = x

        return len(self.visible_trees.keys())

    def calculate_trees(self, what: np.ndarray, num: int) -> int:
        """Calculate the trees matching the criteria"""
        count = 0
        for item in what:
            if item < num:
                count += 1
            else:
                count += 1
                break

        return count

    def part2(self) -> int:
        """Get the second part result"""
        trees_view = {}
        max_count = 0

        for index, num in self.visible_trees.items():
            if index[0] == 0 or index[1] == 0:
                continue
            total_count = 1

            prev_row = self.trees[index[0], : index[1]][::-1]
            total_count *= self.calculate_trees(what=prev_row, num=num)

            next_row = self.trees[index[0], index[1] + 1 :]
            total_count *= self.calculate_trees(what=next_row, num=num)

            prev_col = self.trees[: index[0], index[1]][::-1]
            total_count *= self.calculate_trees(what=prev_col, num=num)

            next_col = self.trees[index[0] + 1 :, index[1]]
            total_count *= self.calculate_trees(what=next_col, num=num)

            trees_view[index] = total_count
            max_count = max(max_count, total_count)

        return max_count


def main() -> None:
    """Do the tasks"""
    game = TreeScout()
    game.load_game(file_name="input8.txt")
    print(game.part1())
    print(game.part2())


if __name__ == "__main__":
    main()


def test_part1() -> None:
    """Tester for part 1"""
    test_game = TreeScout()
    test_game.load_game(file_name="input8_test.txt")
    assert test_game.part1() == 21


def test_part2() -> None:
    """Tester for part 2"""
    test_game = TreeScout()
    test_game.load_game(file_name="input8_test.txt")

    test_game.part1()
    assert test_game.part2() == 8
