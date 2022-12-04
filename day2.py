#!/usr/bin/env python
""" AoC 2022 Day 2"""


class OneRound:
    """Process one round"""

    item_value = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    winners = {"A": "Z", "B": "X", "C": "Y"}
    equals = {"A": "X", "B": "Y", "C": "Z"}
    losers = {"A": "Y", "B": "Z", "C": "X"}
    win_value = 6
    equal_value = 3

    def __init__(self, round_id: int, opponent: str, my_item: str) -> None:
        self.round = round_id
        self.opponent = opponent
        self.my_item = my_item
        self.score_round_1 = 0
        self.score_round_2 = 0

    def calculate_score_round_1(self) -> None:
        """Calculate the result of the round"""

        self.score_round_1 = self.item_value[self.my_item]

        if self.my_item == self.equals[self.opponent]:
            self.score_round_1 += self.equal_value

        if self.my_item == self.losers[self.opponent]:
            self.score_round_1 += self.win_value

    def calculate_score_round_2(self) -> None:
        """Calculate the result of the round"""

        if self.my_item == "X":
            self.score_round_2 += self.item_value[self.winners[self.opponent]]

        if self.my_item == "Y":
            self.score_round_2 += self.item_value[self.equals[self.opponent]]
            self.score_round_2 += self.equal_value

        if self.my_item == "Z":
            self.score_round_2 += self.item_value[self.losers[self.opponent]]
            self.score_round_2 += self.win_value


class Game:
    """Play the game rounds"""

    def __init__(self) -> None:
        self.rounds: list[OneRound] = []
        self.total_score_round_1 = 0
        self.total_score_round_2 = 0

    def load_game(self, file_name: str) -> None:
        """Load the egame from the input"""

        with open(file_name, encoding="UTF-8") as in_file:
            rounds = [line.split(" ") for line in in_file.read().split("\n")]

        for round_id, one_round in enumerate(rounds):
            try:
                next_round = OneRound(
                    round_id=round_id, opponent=one_round[0], my_item=one_round[1]
                )
                self.rounds.append(next_round)
            except IndexError:
                pass

    def calculate_scores(self) -> None:
        """Calculate scores for Task 1 and Task 2"""

        for next_round in self.rounds:
            next_round.calculate_score_round_1()
            next_round.calculate_score_round_2()

            self.total_score_round_1 += next_round.score_round_1
            self.total_score_round_2 += next_round.score_round_2


def main() -> None:
    test_game = Game()
    test_game.load_game(file_name="input2_test.txt")
    test_game.calculate_scores()
    assert test_game.total_score_round_1 == 15
    assert test_game.total_score_round_2 == 12

    game = Game()
    game.load_game(file_name="input2.txt")
    game.calculate_scores()
    print(game.total_score_round_1)
    print(game.total_score_round_2)


if __name__ == "__main__":
    main()
