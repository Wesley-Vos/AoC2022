from sortedcontainers import SortedList


class SpecialList:
    def __init__(self, size):
        self.size = size
        self._list = SortedList()

    def add(self, val):
        if len(self._list) > 0 and len(self._list) == self.size and val < self._list[0]:
            return
        self._list.add(val)

    def __getitem__(self, index):
        return list[index]


class Day1():
    def __init__(self):
        self.elves_inventory_sums = SortedList()
        elf_inventory_sum = 0
        with open("input.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    elves_inventory_sums.add(elf_inventory_sum)
                    elf_inventory_sum = 0
                else:
                    elf_inventory_sum += int(line)

    def solve_part1(self):
        return self.elves_inventory_sum[-1]

    def solve_part2(self):
        return sum(self.elves_inventory_sum[:3])


def main():
    day1 = Day1()
    print(day1.solve_part1())


if __name__ == "__main__":
    main()

