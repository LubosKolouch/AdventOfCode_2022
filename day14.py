#!/usr/bin/env python
""" AoC 2022 Day 14"""
from collections import defaultdict


class Grid:
    """Process the signals"""

    def __init__(self) -> None:
        self.grid: defaultdict = defaultdict(str)
        self.grid_max_x = 500
        self.grid_min_x = 500
        self.grid_max_y = 0

    def print_grid(self) -> None:
        """print the grid"""

        for y in range(0, self.grid_max_y + 3):
            for x in range(self.grid_min_x - 7, self.grid_max_x + 10):
                if self.grid[(x, y)] == "#":
                    print("█", end="")
                elif self.grid[(x, y)] == "o":
                    print("o", end="")
                else:
                    print(" ", end="")
            print("")

    def load_game(self, file_name: str) -> None:
        """Load the game from the input"""

        with open(file_name, encoding="UTF-8") as in_file:
            self.layout = [line.split("->") for line in in_file.read().split("\n")]
            for line in self.layout:
                if not line[0]:
                    continue
                curx, cury = list(map(int, line[0].split(",")))
                self.grid[(curx, cury)] = "#"
                for coord in line[1:]:
                    newx, newy = list(map(int, coord.split(",")))

                    # v
                    if curx == newx and cury < newy:
                        for i in range(cury + 1, newy + 1):
                            self.grid[(curx, i)] = "#"

                    # ^
                    if curx == newx and cury > newy:
                        for i in range(cury, newy - 1, -1):
                            self.grid[(curx, i)] = "#"

                    # v
                    if cury == newy and curx < newx:
                        for i in range(curx + 1, newx + 1):
                            self.grid[(i, cury)] = "#"

                    # v
                    if cury == newy and curx > newx:
                        for i in range(curx, newx - 1, -1):
                            self.grid[(i, cury)] = "#"

                    self.grid_max_y = max(cury, newy, self.grid_max_y)
                    self.grid_max_x = max(curx, newx, self.grid_max_x)
                    self.grid_min_x = min(curx, newx, self.grid_min_x)

                    curx, cury = newx, newy

    def part(self, part: int = 1) -> int:
        """Get the part result"""

        if part == 2:
            for i in range(-100000, self.grid_max_x + 100000):
                self.grid[(i, self.grid_max_y + 2)] = "#"
            self.grid_max_y += 2

        grain_x = 500
        grain_y = 0

        my_round = 0

        while 1:
            my_round += 1
            if part == 1:
                if grain_y > self.grid_max_y:
                    break
            else:
                if my_round > 1 and grain_x == 500 and grain_y == 0:
                    break

            grain_x = 500
            grain_y = 0

            self.grid[(grain_x, grain_y)] = "o"

            while 1:
                if grain_y > self.grid_max_y:
                    break
                if self.grid[(grain_x, grain_y + 1)] in ["#", "o"]:
                    if self.grid[(grain_x - 1, grain_y + 1)] in ["#", "o"]:
                        if self.grid[(grain_x + 1, grain_y + 1)]:
                            # sand is stable
                            break
                        else:
                            self.grid[(grain_x, grain_y)] = ""
                            self.grid[(grain_x + 1, grain_y + 1)] = "o"
                            grain_x += 1
                            grain_y += 1
                    else:
                        self.grid[(grain_x, grain_y)] = ""
                        self.grid[(grain_x - 1, grain_y + 1)] = "o"
                        grain_x -= 1
                        grain_y += 1
                else:
                    self.grid[(grain_x, grain_y)] = ""
                    self.grid[(grain_x, grain_y + 1)] = "o"
                    grain_y += 1

            # self.print_grid()

        if part == 1:
            return my_round - 2

        return my_round - 1


def main() -> None:
    """Do the tasks"""
    game = Grid()
    game.load_game(file_name="input14.txt")
    print(game.part())
    game = Grid()
    game.load_game(file_name="input14.txt")
    print(game.part(part=2))


if __name__ == "__main__":
    main()


def test_part1() -> None:
    """Tester for part 1"""
    test_game = Grid()
    test_game.load_game(file_name="input14_test.txt")
    assert test_game.part() == 24


def test_part2() -> None:
    """Tester for part 2"""
    test_game = Grid()
    test_game.load_game(file_name="input14_test.txt")
    assert test_game.part(part=2) == 93
