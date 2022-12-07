from collections import deque
import re


class Day5:
    def __init__(self, filename):
        self.filename = filename

    def solve_part1(self):
        # pattern = "(\ {3,4})|(\[[A-Z]\]\ ?)"
        pattern = '(.(.)..?)|(\[([A-Z])\].?)'
        stacks = []

        with open(self.filename, "r") as f:
            cnt = 0
            readingInitStack = True
            temp_stacks = []

            for row in f:
                row = row.split("\n")[0]
                if row == "":
                    readingInitStack = False

                    for i, temp_stack in enumerate(temp_stacks):
                        temp_stack.reverse()
                        stacks.append(temp_stack)

                    # print(stacks)
                    cnt += 1
                    continue

                if readingInitStack:
                    crates = list(map(lambda crate: crate[1], re.findall(pattern, row)))

                    if cnt == 0:
                        temp_stacks = [deque() for _ in range(len(crates))]

                    for i, crate in enumerate(crates):
                        if crate != ' ' and crate.isalpha():
                            temp_stacks[i].append(crate)
                else:
                    # print("Movement", row)
                    pattern2 = '(\d+)'
                    number_of_creates, from_stack, to_stack = tuple(map(int, re.findall(pattern2, row)))
                    # print(number_of_creates, from_stack, to_stack)

                    for _ in range(number_of_creates):
                        stacks[to_stack - 1].append(stacks[from_stack - 1].pop())

                cnt += 1

                # print(row.split("\n")[0], pattern)
                # crates = list(map(lambda crate: list(filter(lambda c: c != "", crate))[0].strip(), re.findall(pattern, row.split("\n")[0])))
        return ''.join(map(lambda stack: stack.pop(), stacks))

    def solve_part2(self):
        pattern = '(.(.)..?)|(\[([A-Z])\].?)'
        stacks = []

        with open(self.filename, "r") as f:
            cnt = 0
            readingInitStack = True
            temp_stacks = []

            for row in f:
                row = row.split("\n")[0]
                if row == "":
                    readingInitStack = False
                    cnt += 1

                    for i, temp_stack in enumerate(temp_stacks):
                        temp_stack.reverse()
                        stacks.append(temp_stack)

                    print(stacks)
                    continue

                if readingInitStack:
                    crates = list(map(lambda crate: crate[1], re.findall(pattern, row)))

                    if cnt == 0:
                        temp_stacks = [deque() for _ in range(len(crates))]

                    for i, crate in enumerate(crates):
                        if crate != ' ' and crate.isalpha():
                            temp_stacks[i].append(crate)
                else:
                    # print("Movement", row)
                    pattern2 = '(\d+)'
                    number_of_creates, from_stack, to_stack = tuple(map(int, re.findall(pattern2, row)))
                    # print(number_of_creates, from_stack, to_stack)

                    move_stack = deque()
                    for _ in range(number_of_creates):
                        move_stack.append(stacks[from_stack - 1].pop())

                    for _ in range(number_of_creates):
                        stacks[to_stack - 1].append(move_stack.pop())

                cnt += 1

                # print(row.split("\n")[0], pattern)
                # crates = list(map(lambda crate: list(filter(lambda c: c != "", crate))[0].strip(), re.findall(pattern, row.split("\n")[0])))
        return ''.join(map(lambda stack: stack.pop(), stacks))


def main():
    day = Day5("input2.txt")
    print(day.solve_part1())
    print(day.solve_part2())


if __name__ == "__main__":
    main()
