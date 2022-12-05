import functools


class Day4():
    def __init__(self):
        pass

    def solve_part1(self):
        cnt = 0
        with open("input2.txt") as f:
            for pair in f:
                elf1, elf2 = list(map(lambda elf: list(map(int, elf.split("-"))), pair.split(",")))
                cnt += (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf2[0] <= elf1[0] and elf2[1] >= elf1[1]) 
            return cnt

    def solve_part2(self):
        with open("input2.txt", "r") as f:
            cnt = 0

            for pair in f:
                elf1, elf2 = list(map(lambda elf: list(map(int, elf.split("-"))), pair.split(",")))
                cnt += elf1[0] <= elf2[1] and elf2[0] <= elf1[1]
            return cnt

def main():
    day = Day4()
    print(day.solve_part1())
    print(day.solve_part2())


if __name__ == "__main__":
    main()
