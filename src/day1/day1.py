from abc import ABC

from sortedcontainers import SortedList


class SpecialList(SortedList, ABC):
    def __init__(self, size):
        super().__init__()
        self.size = size

    def add(self, val):
        if super().__len__() == self.size:
            if val > super().__getitem__(0):
                super().pop(0)
            else:
                return
        super().add(val)


class Day1:
    def __init__(self):
        self.elves_inventory_sums = SpecialList(3)
        elf_inventory_sum = 0
        with open("input.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    self.elves_inventory_sums.add(elf_inventory_sum)
                    elf_inventory_sum = 0
                else:
                    elf_inventory_sum += int(line)

    def solve_part1(self):
        return self.elves_inventory_sums[-1]

    def solve_part2(self):
        return sum(self.elves_inventory_sums[:3])


def main():
    day1 = Day1()
    print(day1.solve_part1())
    print(day1.solve_part2())


if __name__ == "__main__":
    main()
