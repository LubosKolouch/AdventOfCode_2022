#!/usr/bin/env python
""" AoC 2022 Day 11"""
import re
from math import floor


class Monkey:
    def __init__(self) -> None:
        self.monkey_id: int
        self.items: list[int] = []
        self.operation: list[str] = []
        self.test: int
        self.test_ok_id: int
        self.test_fail_id: int
        self.items_count: int = 0

    def __str__(self) -> str:
        return (
            f"id: {self.monkey_id} "
            f"items: {self.items} "
            f"operation: {self.operation} "
            f"test: {self.test} "
            f"test_ok: {self.test_ok_id} "
            f"test_fail: {self.test_fail_id} "
            f"counted items: {self.items_count} "
        )


class Monkeys:
    """Process the signals"""

    def __init__(self) -> None:
        self.monkeys: list[Monkey] = []
        self.mod_num: int = 1

    def load_game(self, file_name: str) -> None:
        """Load the game from the input"""

        with open(file_name, encoding="UTF-8") as in_file:
            monkey_list = [
                item
                for item in [
                    lines.split("\n") for lines in in_file.read().split("\n\n")
                ]
            ]

        for item in monkey_list:
            monkey = Monkey()
            if monkey_id := re.search(r"\d+", item[0]):
                monkey.monkey_id = int(monkey_id.group(0))

            if starting_list := re.findall(r"\d+", item[1]):
                monkey.items = list(map(int, starting_list))

            operation = item[2].split("new = old ")
            monkey.operation = operation[1].split(" ")

            if test := re.search(r"\d+", item[3]):
                monkey.test = int(test.group(0))
                self.mod_num *= monkey.test

            if test_ok_id := re.search(r"\d+", item[4]):
                monkey.test_ok_id = int(test_ok_id.group(0))

            if test_fail_id := re.search(r"\d+", item[5]):
                monkey.test_fail_id = int(test_fail_id.group(0))

            self.monkeys.append(monkey)

    def part(self, rounds: int, part: int = 1) -> int:
        """Get the first part result"""

        for my_round in range(rounds):

            for monkey in self.monkeys:

                for _ in range(len(monkey.items)):
                    monkey.items_count += 1
                    item = monkey.items.pop()

                    if monkey.operation[0] == "*":
                        if monkey.operation[1] == "old":
                            item *= item
                        else:
                            item *= int(monkey.operation[1])

                    else:
                        if monkey.operation[1] == "old":
                            item += item
                        else:
                            item += int(monkey.operation[1])

                    if part == 1:
                        item = floor(item / 3)

                    item = item % self.mod_num
                    if item % monkey.test == 0:
                        self.monkeys[monkey.test_ok_id].items.append(item)
                        self.monkeys[monkey.test_ok_id].items.sort()
                    else:
                        self.monkeys[monkey.test_fail_id].items.append(item)
                        self.monkeys[monkey.test_fail_id].items.sort()

        best_values = [monkey.items_count for monkey in self.monkeys]

        best_values.sort()

        return best_values[-1] * best_values[-2]

    def part2(self) -> int:
        """Get the second part result"""


def main() -> None:
    """Do the tasks"""
    game = Monkeys()
    game.load_game(file_name="input11.txt")
    print(game.part(rounds=20))

    game = Monkeys()
    game.load_game(file_name="input11.txt")
    print(game.part(rounds=10000, part=2))


if __name__ == "__main__":
    main()


def test_part1() -> None:
    """Tester for part 1"""
    test_game = Monkeys()
    test_game.load_game(file_name="input11_test.txt")
    assert test_game.part(rounds=20) == 10605


def test_part2() -> None:
    test_game = Monkeys()
    test_game.load_game(file_name="input11_test.txt")
    assert test_game.part(rounds=10000, part=2) == 2713310158
