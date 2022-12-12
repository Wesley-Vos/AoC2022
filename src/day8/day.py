
class Grid:
    def __init__(self, filename):
        self._grid = self._get_input(filename)
        self._score_table = [[0 for _ in range(len(self._grid[y]))] for y in range(len(self._grid))]

    def _get_input(self, filename):
        storage = []
        with open(filename, "r") as file:
            for row in file:
                storage.append(list(map(int, row.strip())))
        return storage

    def get(self, x, y):
        return self._grid[y][x]

    def _is_edge(self, x, y):
        return x == 0 or y == 0 or x == (len(self._grid[0]) - 1) or y == (len(self._grid) - 1)

    def _is_inner_visible(self, x, y):
        row = self._grid[y]
        col = [self.get(x, y) for y in range(len(self._grid))]

        tree = self.get(x, y)
        left_approach = max(row[0:x]) < tree
        right_approach = max(row[(x + 1):]) < tree
        up_approach = max(col[0:y]) < tree
        bottom_approach = max(col[(y + 1):]) < tree

        return left_approach or right_approach or up_approach or bottom_approach

    def _is_visible(self, x, y):
        return self._is_edge(x, y) or self._is_inner_visible(x, y)

    def print(self):
        print("###### START GRID ########")
        for y in range(len(self._grid)):
            res = ""
            for x in range(len(self._grid[y])):
                res += "1" if self._is_visible(x, y) else "0"
            print(res)
        print("###### END GRID ########")

    def cnt_visible_trees(self):
        return sum(sum(self._is_visible(x, y) for x in range(len(self._grid[y]))) for y in range(len(self._grid)))

    def _get_view_distance(self, x, y, dir):
        tree = self.get(x, y)
        match dir:
            case "up":
                if y == 0:
                    return 0
                cnt = 0
                y2 = y - 1
                while y2 >= 0:
                    cnt += 1
                    if self.get(x, y2) >= tree:
                        break

                    y2 -= 1
                return cnt
            case "down":
                if y == (len(self._grid) - 1):
                    return 0
                cnt = 0
                y2 = y + 1
                while y2 < len(self._grid):
                    # print(self.get(x, y2))
                    cnt += 1
                    if self.get(x, y2) >= tree:
                        break

                    y2 += 1
                return cnt
            case "left":
                if x == 0:
                    return 0
                cnt = 0
                x2 = x - 1
                while x2 >= 0:
                    cnt += 1
                    if self.get(x2, y) >= tree:
                        break

                    x2 -= 1
                return cnt
            case "right":
                if x == (len(self._grid[y]) - 1):
                    return 0
                cnt = 0
                x2 = x + 1
                while x2 < len(self._grid[y]):
                    cnt += 1
                    if self.get(x2, y) >= tree:
                        break

                    x2 += 1
                return cnt

    def _determine_scenic_scores(self):
        for y in range(len(self._grid)):
            for x in range(len(self._grid[y])):
                val = 1
                dirs = ["up", "down", "left", "right"]
                for dir in dirs:
                    val2 = self._get_view_distance(x, y, dir)
                    val *= val2
                self._score_table[y][x] = val

    def find_highest_scenic_score(self):
        self._determine_scenic_scores()
        return max(*[max(row) for row in self._score_table])


class Day8:
    input = None

    def __init__(self, filename):
        self.grid = Grid(filename)

    def solve_part1(self):
        return self.grid.cnt_visible_trees()

    def solve_part2(self):
        return self.grid.find_highest_scenic_score()


def main():
    day = Day8("input2.txt")
    print(f"Part 1 solution: { day.solve_part1() }")
    print(f"Part 2 solution: {day.solve_part2() }")


if __name__ == "__main__":
    main()
