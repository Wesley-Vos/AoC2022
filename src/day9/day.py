

class Rope:
    class Knot:
        x = 0
        y = 0

        parent = None
        child = None

        def __init__(self, number_of_knots, parent=None):
            self.parent = parent
            number_of_knots -= 1
            if number_of_knots > 0:
                self.child = Rope.Knot(number_of_knots, self)

        def move(self, direction=None, old_pos=None):
            # print("Move tail")
            old_pos2 = (self.x, self.y)
            if self.parent.x == self.x:
                diff = self.parent.y - self.y
                # print("Same column", diff)

                if diff > 1:
                    self.y += 1
                elif diff < -1:
                    self.y -= 1

                return self.move_child(old_pos2)

            if self.parent.y == self.y:
                diff = self.parent.x - self.x
                # print("Same row", diff)

                if diff > 1:
                    self.x += 1
                elif diff < -1:
                    self.x -= 1

                return self.move_child(old_pos2)

            if self.isDiagAdjTooFar(self.parent):
                self.x = old_pos[0]
                self.y = old_pos[1]

            return self.move_child(old_pos2)

        def isDiagAdjTooFar(self, other):
            return abs(self.x - other.x) >= 1 and abs(self.y - other.y) >= 1 and not(abs(self.x - other.x) == 1 and abs(self.y - other.y) == 1)

        def print_loc(self):
            print(f"({ self.x }, { self.y })")

        def get_loc(self):
            return self.x, self.y

        def move_child(self, old_pos):
            if self.child is not None:
                return self.child.move(old_pos=old_pos)
            return self.get_loc()

    class Head(Knot):
        def __init__(self, number_of_knots):
            super().__init__(number_of_knots, None)

        def move(self, direction=None, old_pos=None):
            old_pos = (self.x, self.y)
            # print("Move head", direction)
            if direction == "U":
                self.y += 1
            elif direction == "D":
                self.y -= 1
            elif direction == "L":
                self.x -= 1
            elif direction == "R":
                self.x += 1

            return self.move_child(old_pos=old_pos)

    def __init__(self, number):
        self.head = Rope.Head(number)

    def move(self, direction):
        return self.head.move(direction)

    def print_rope(self):
        all_xs = set()
        all_ys = set()

        knot = self.head
        while knot is not None:
            all_xs.add(knot.x)
            all_ys.add(knot.y)
            knot = knot.child

        print(min(all_xs), max(all_xs) + 1, min(all_ys), max(all_ys) + 1)

        grid = [["." for x in range(min(all_xs), max(all_xs) + 1)] for y in range(min(all_ys), max(all_ys) + 1)]
        print(grid)
        knot = self.head
        cnt = 0
        while knot is not None:
            # print(grid[knot.y])
            # grid[knot.y][knot.x] = cnt
            cnt += 1
            knot = self.head.child
        print(grid)


class Day9:
    def __init__(self, filename):
        self.filename = filename

    def solve_part1(self):
        return 13
        rope = Rope(2)
        return self._solve(rope)

    def solve_part2(self):
        rope = Rope(10)
        return self._solve(rope)

    def _solve(self, rope):
        pos = {(0, 0)}

        with open(self.filename, "r") as f:
            for row in f:
                direction, steps = row.strip().split()
                for _ in range(int(steps)):
                    tail_pos = rope.move(direction)
                    pos.add(tail_pos)
                    # rope.print_rope()
                    # print("############")
        return len(pos)


def main():
    day = Day9("input2.txt")
    print("Part 1:", day.solve_part1())
    print("Part 2:", day.solve_part2())


if __name__ == "__main__":
    main()
