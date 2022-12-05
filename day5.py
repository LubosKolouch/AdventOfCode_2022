#!/usr/bin/env python
""" AoC 2022 Day 5"""
import re
from collections import deque
from copy import deepcopy


class BoxMover:
    """Process the boxes"""

    def __init__(self) -> None:
        self.box_queue: dict[int, deque[str]] = {}
        self.instr_list: list[list[int]] = []
        for i in range(9):
            self.box_queue[i + 1] = deque()

    def load_game(self, file_name: str) -> None:
        """Load the game from the input"""

        with open(file_name, encoding="UTF-8") as in_file:
            box_queue = [x.split("\n") for x in in_file.read().split("\n\n")]

        for line in box_queue[0]:
            for i in range(9):
                try:
                    if not re.match(r"[\s*\d+]", line[1 + i * 4]):
                        self.box_queue[i + 1].append(line[1 + i * 4])
                except IndexError:
                    continue

        for line in box_queue[1]:
            try:
                match = re.search(r"move (\d+) from (\d+) to (\d+)", line)
                if match:
                    matches = match.groups()
                    instr = list(map(int, matches))
                    self.instr_list.append(instr)
            except AttributeError:
                continue

    def part1(self) -> str:
        """Get the first part result"""
        box_queue = deepcopy(self.box_queue)
        for instr in self.instr_list:
            for _ in range(instr[0]):
                box = box_queue[instr[1]].popleft()
                box_queue[instr[2]].appendleft(box)

        result = ""
        for i in range(9):
            try:
                result += box_queue[i + 1].popleft()
            except IndexError:
                pass

        return result

    def part2(self) -> str:
        """Get the second part result"""
        box_queue = deepcopy(self.box_queue)

        for instr in self.instr_list:

            box_temp_queue: list[str] = []
            for _ in range(instr[0]):
                box = box_queue[instr[1]].popleft()
                box_temp_queue.insert(0, box)

            box_queue[instr[2]].extendleft(box_temp_queue)

        result = ""
        for i in range(9):
            try:
                result += box_queue[i + 1].popleft()
            except IndexError:
                pass

        return result


def main() -> None:
    """Do the tasks"""
    game = BoxMover()
    game.load_game(file_name="input5.txt")
    print(game.part1())
    print(game.part2())


if __name__ == "__main__":
    main()


def test_part1() -> None:
    """Tester for part 1"""
    test_game = BoxMover()
    test_game.load_game(file_name="input5_test.txt")
    assert test_game.part1() == "CMZ"


def test_part2() -> None:
    """Tester for part 2"""
    test_game = BoxMover()
    test_game.load_game(file_name="input5_test.txt")
    assert test_game.part2() == "MCD"
