#!/usr/bin/env python
""" AoC 2022 Day 3"""


class Rucksack:
    """Rucksack sorter"""

    def __init__(self, content: str) -> None:
        self.content = content
        self.first_half = content[0 : len(content) // 2]
        self.second_half = content[len(content) // 2 :]

    def find_offending_chars(self) -> set:
        """Find the duplicates"""
        return set(self.first_half).intersection(set(self.second_half))


class RuckSorter:
    """Process the rucksacks"""

    def __init__(self) -> None:
        self.rucksacks: list[Rucksack] = []

    def get_char_value(self, what: str) -> int:
        """Convert the char to value"""
        if what.islower():
            return ord(what) - ord("a") + 1
        return ord(what) - ord("A") + 27

    def load_game(self, file_name: str) -> None:
        """Load the game from the input"""

        with open(file_name, encoding="UTF-8") as in_file:
            sacks = in_file.read().split("\n")

        for sack in sacks:
            try:
                one_sack = Rucksack(content=sack)
                self.rucksacks.append(one_sack)
            except IndexError:
                pass

    def part1(self) -> int:
        """Get the first part result"""
        score = 0

        for sack in self.rucksacks:
            problem_chars = sack.find_offending_chars()

            for one_char in problem_chars:
                score += self.get_char_value(one_char)
        return score

    def part2(self) -> int:
        """Get the second part result"""
        score = 0
        pos = 0

        while 1:
            try:
                problem_chars = (
                    set(self.rucksacks[pos].content)
                    .intersection(set(self.rucksacks[pos + 1].content))
                    .intersection(set(self.rucksacks[pos + 2].content))
                )
                for one_char in problem_chars:
                    score += self.get_char_value(one_char)

                pos += 3
            except IndexError:
                break

        return score


def main() -> None:
    game = RuckSorter()
    game.load_game(file_name="input3.txt")
    print(game.part1())
    print(game.part2())


if __name__ == "__main__":
    main()


def test_part1():
    """Tester for part 1"""
    test_game = RuckSorter()
    test_game.load_game(file_name="input3_test.txt")
    assert test_game.part1() == 157


def test_part2():
    """Tester for part 2"""
    test_game = RuckSorter()
    test_game.load_game(file_name="input3_test.txt")
    assert test_game.part2() == 70
