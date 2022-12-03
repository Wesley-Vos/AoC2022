import functools


class Day3():
    def __init__(self):
        pass

    @staticmethod
    def char_to_prio(char):
        return (ord(char) - 65 + 27) if ord(char) < 91 else (ord(char) - 96)

    def solve_part1(self):
        sum_val = 0

        with open("input2.txt") as f:
            for rucksack in f:
                mdl = len(rucksack) // 2
                rucksack = rucksack.strip()
                intersect = set(rucksack[:mdl]).intersection(set(rucksack[mdl:]))
                sum_val += self.char_to_prio(list(intersect)[0])
        return sum_val

    def solve_part2(self):
        with open("input2.txt", "r") as f:
            cnt = 0
            sum_val = 0
    
            for rucksack in f:
                rucksack = set(list(rucksack.strip()))
                shared = rucksack if (cnt % 3) == 0 else shared.intersection(rucksack)
                sum_val += self.char_to_prio(list(shared)[0]) if (cnt % 3 == 2) else 0
                cnt += 1 
        return sum_val


def main():
    day3 = Day3()
    print(day3.solve_part1())
    print(day3.solve_part2())


if __name__ == "__main__":
    main()
