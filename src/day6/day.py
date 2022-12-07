class Day6:
    def __init__(self, filename):
        with open(filename, "r") as file:
            self._input = file.readline().strip()

    def _solve(self, length):
        hist = []

        for i, char in enumerate(self._input):
            if i >= length:
                hist.pop(0)
            hist.append(char)

            if i >= (length - 1):
                if len(set(hist)) == length:
                    return i + 1

    def solve_part1(self):
        return self._solve(4)

    def solve_part2(self):
        return self._solve(14)


def main():
    day = Day6("input.txt")
    print(day.solve_part1())
    print(day.solve_part2())


if __name__ == "__main__":
    main()