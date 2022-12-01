#!/usr/bin/env python
class Elf:
    def __init__(self, elf_id: int) -> None:
        self.elf_id = elf_id
        self.calorie_list: list[int] = []
        self.total_calories = 0


class Expedition:
    def __init__(self) -> None:
        self.elves: list[Elf] = []

    def get_solutions(self) -> None:
        """Get the 3 elves with the most calories"""

        self.elves.sort(key=lambda x: x.total_calories, reverse=True)
        print(f"Task1: {self.elves[0].total_calories}")

        total = 0
        for i in range(0, 3):
            total += self.elves[i].total_calories

        print(f"Task2: {total}")

    def load_expedition(self) -> None:
        """Load the expedition from the input"""

        with open("input1.txt", encoding="UTF-8") as in_file:
            elves = [line.split("\n") for line in in_file.read().split("\n\n")]

        for elf_pos, each_elf in enumerate(elves):
            elf = Elf(elf_pos)

            for calorie in each_elf:
                try:
                    elf.calorie_list.append(int(calorie))
                    elf.total_calories += int(calorie)

                except ValueError:
                    pass
            self.elves.append(elf)


def main() -> None:
    expedition = Expedition()
    expedition.load_expedition()
    expedition.get_solutions()


if __name__ == "__main__":
    main()
