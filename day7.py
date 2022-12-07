#!/usr/bin/env python
""" AoC 2022 Day 7"""
import re
from collections import Counter, deque
from copy import deepcopy


class FoldersProcessor:
    """Process the signals"""

    def __init__(self) -> None:
        self.instr_list: list
        self.folders: dict = {}
        self.folders["/"] = 0

    def load_game(self, file_name: str) -> None:
        """Load the game from the input"""

        with open(file_name, encoding="UTF-8") as in_file:
            instr_list = in_file.read().split("\n")

        self.instr_list = instr_list

    def part1(self) -> int:
        """Get the first part result"""
        folders_pos: deque = deque()
        for instr in self.instr_list:
            if instr.startswith("$ cd"):

                if ".." in instr:
                    folders_pos.popleft()

                elif "/" in instr:
                    folders_pos.clear()
                    folders_pos.append("/")

                else:
                    what = instr.split(" ")[2]
                    folders_pos.appendleft(f"{folders_pos[0]}{what}/")

                    if self.folders.get(folders_pos[0], {}) == {}:
                        self.folders[folders_pos[0]] = 0

            elif match := re.match(r"(\d+) (\w+)", instr):
                deque_copy = deepcopy(folders_pos)
                for folder in deque_copy:
                    self.folders[folder] = self.folders.get(folder, 0) + int(
                        match.groups()[0]
                    )

        size = 0
        for _, item in self.folders.items():
            if item < 100000:
                size += item

        return size

    def part2(self) -> int:
        """Get the second part result"""

        total_space = 70000000
        needed_space = 30000000

        free_space = total_space - self.folders["/"]

        min_folder = total_space
        for item in self.folders.values():
            if free_space + item >= needed_space and item < min_folder:
                min_folder = item

        return min_folder


def main() -> None:
    """Do the tasks"""
    game = FoldersProcessor()
    game.load_game(file_name="input7.txt")
    print(game.part1())
    print(game.part2())


if __name__ == "__main__":
    main()


def test_part1() -> None:
    """Tester for part 1"""
    test_game = FoldersProcessor()
    test_game.load_game(file_name="input7_test.txt")
    assert test_game.part1() == 954378


def test_part2() -> None:
    """Tester for part 2"""
    test_game = FoldersProcessor()
    test_game.load_game(file_name="input7_test.txt")
    assert test_game.part2() == 24933642
