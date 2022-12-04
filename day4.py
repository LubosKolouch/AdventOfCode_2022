#!/usr/bin/env python
""" AoC 2022 Day 4"""


class IntervalPair:
    """Interval storage"""

    def __init__(self, pairs: list) -> None:
        self.pairs = pairs
        self.pair_1 = list(map(int, pairs[0].split("-")))
        self.pair_2 = list(map(int, pairs[1].split("-")))

    def compare_overlaps(self) -> bool:
        """Check if the intervals overlap"""

        if self.pair_1[0] >= self.pair_2[0] and self.pair_1[1] <= self.pair_2[1]:
            return True

        if self.pair_2[0] >= self.pair_1[0] and self.pair_2[1] <= self.pair_1[1]:
            return True

        return False

    def check_if_overlap_at_all(self) -> bool:
        """Check if there is any overlap"""

        if self.pair_1[1] < self.pair_2[0] or self.pair_2[1] < self.pair_1[0]:
            return False

        return True


class Intervals:
    """Process the intervals"""

    def __init__(self) -> None:
        self.intervals: list[IntervalPair] = []

    def get_char_value(self, what: str) -> int:
        """Convert the char to value"""
        if what.islower():
            return ord(what) - ord("a") + 1
        return ord(what) - ord("A") + 27

    def load_game(self, file_name: str) -> None:
        """Load the game from the input"""

        with open(file_name, encoding="UTF-8") as in_file:
            intervals = [x.split(",") for x in in_file.read().split("\n")]

        for interval in intervals:
            try:
                one_interval = IntervalPair(pairs=interval)
                self.intervals.append(one_interval)
            except ValueError:
                pass

    def part1(self) -> int:
        """Get the first part result"""
        score = 0
        for interval in self.intervals:
            if interval.compare_overlaps():
                score += 1

        return score

    def part2(self) -> int:
        """Get the second part result"""
        score = 0
        for interval in self.intervals:
            if interval.check_if_overlap_at_all():
                score += 1

        return score


def main() -> None:
    game = Intervals()
    game.load_game(file_name="input4.txt")
    print(game.part1())
    print(game.part2())


if __name__ == "__main__":
    main()


def test_part1():
    """Tester for part 1"""
    test_game = Intervals()
    test_game.load_game(file_name="input4_test.txt")
    assert test_game.part1() == 2


def test_part2():
    """Tester for part 2"""
    test_game = Intervals()
    test_game.load_game(file_name="input4_test.txt")
    assert test_game.part2() == 4
