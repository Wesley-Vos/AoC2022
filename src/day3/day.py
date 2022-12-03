import functools


class Day3():
    def __init__(self):
        pass

    @staticmethod
    def transform_rucksack(char):
        return (ord(char) - 65 + 27) if ord(char) < 91 else (ord(char) - 96)

    def solve_part1(self):
        sum_val = 0

        with open("input2.txt") as f:
            for rucksack in f:
                char_list = [0 for i in range(53)]
                middle = len(rucksack) // 2
                rucksack = map(self.transform_rucksack, rucksack.strip())

                for i, val in enumerate(rucksack):
                    if i >= middle:
                        if char_list[val] > 0:
                            sum_val += val
                            break
                    else:
                        char_list[val] += 1

        return sum_val

    def solve_part2(self):
        with open("input2.txt", "r") as f:
            cnt = 0
            sum_val = 0

            def reducer(result, val):
                result[val] = True
                return result

            for rucksack_line in f:
                rucksack = functools.reduce(reducer, map(self.transform_rucksack, rucksack_line.strip()), [False for _ in range(53)])

                if (cnt % 3) == 0:
                    group = rucksack

                group = [g and r for g, r in zip(group, rucksack)]
                if (cnt % 3) == 2:
                    sum_val += [i for i, x in enumerate(group) if x][0]
                cnt += 1
        return sum_val


def main():
    day3 = Day3()
    print(day3.solve_part1())
    print(day3.solve_part2())


if __name__ == "__main__":
    main()
