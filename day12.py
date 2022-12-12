#!/usr/bin/env python
""" AoC 2022 Day 12"""
import networkx as nx
import numpy as np
from networkx.exception import NetworkXNoPath


class Grid:
    """Process the signals"""

    def __init__(self) -> None:
        self.grid: np.ndarray
        self.g = nx.DiGraph()
        self.starting_positions_2: list[tuple] = []
        self.end_pos: tuple

    def load_game(self, file_name: str) -> None:
        """Load the game from the input"""

        self.grid = np.genfromtxt(file_name, delimiter=1, dtype=str)

    def part1(self) -> int:
        """Get the first part result"""

        start_pos = (0, 0)
        for index, item in np.ndenumerate(self.grid):
            if item == "S":
                self.grid[index] = "a"
                item = "a"
                start_pos = index

            if item == "E":
                self.grid[index] = "z"
                item = "z"
                self.end_pos = index

            if item == "a":
                self.starting_positions_2.append(index)

            moves: dict = {"R": (0, 1), "U": (-1, 0), "L": (0, -1), "D": (1, 0)}

            for move in moves:
                test_coord = moves[move]
                node_to = (index[0] + test_coord[0], index[1] + test_coord[1])

                if node_to[0] < 0:
                    continue
                if node_to[1] < 0:
                    continue

                try:
                    if ord(self.grid[node_to]) - ord(item) <= 1:
                        self.g.add_edge(index, node_to)
                except IndexError:
                    pass

        path = nx.shortest_path(self.g, source=start_pos, target=self.end_pos)
        return len(path) + 1

    def part2(self) -> int:
        """Get the second part result"""

        result: list[int] = []
        for pos in self.starting_positions_2:
            try:
                path = nx.shortest_path(self.g, source=pos, target=self.end_pos)
                result.append(len(path))

            except NetworkXNoPath:
                pass

        return min(result) + 1


def main() -> None:
    """Do the tasks"""
    game = Grid()
    game.load_game(file_name="input12.txt")
    print(game.part1())
    print(game.part2())


if __name__ == "__main__":
    main()


def test_part1() -> None:
    """Tester for part 1"""
    test_game = Grid()
    test_game.load_game(file_name="input12_test.txt")
    assert test_game.part1() == 31


def test_part2() -> None:
    test_game = Grid()
    test_game.load_game(file_name="input12_test.txt")
    test_game.part1()
    assert test_game.part2() == 29
