import functools


class Day4():
    def __init__(self, filename):
        self.filename = filename

    def pairs(self):
        with open(self.filename, "r") as file:
            for line in file:
                yield list(map(lambda elf: list(map(int, elf.split("-"))), line.split(",")))

    contains = lambda self, a, b: (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1]) 
    overlap = lambda self, a, b: a[0] <= b[1] and b[0] <= a[1] 
    solve = lambda self, func: sum(func(elf1, elf2) for elf1, elf2 in self.pairs())

    def solve_part1(self):
        return self.solve(self.contains)

    def solve_part2(self):
        return self.solve(self.overlap)        

def main():
    day = Day4("input2.txt")
    print(day.solve_part1())
    print(day.solve_part2())


if __name__ == "__main__":
    main()
