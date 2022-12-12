class Rope:
    DIR_MAPPING = {
        "U": (0, 1),
        "D": (0, -1),
        "L": (-1, 0),
        "R": (1, 0)
    }

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

        def move(self, direction=None):
            if abs(self.parent.x - self.x) > 1 or abs(self.parent.y - self.y) > 1:
                if self.parent.y > self.y:
                    self.y += 1
                elif self.parent.y < self.y:
                    self.y -= 1
                if self.parent.x > self.x:
                    self.x += 1
                elif self.parent.x < self.x:
                    self.x -= 1

            return self.move_child()

        def print_loc(self):
            print(f"({ self.x }, { self.y })")

        def get_loc(self):
            return self.x, self.y

        def move_child(self):
            if self.child is not None:
                return self.child.move()
            return self.get_loc()

    class Head(Knot):
        def __init__(self, number_of_knots):
            super().__init__(number_of_knots, None)

        def move(self, direction=None):
            x, y = Rope.DIR_MAPPING[direction]
            self.x += x
            self.y += y

            return self.move_child()

    def __init__(self, number):
        self.head = Rope.Head(number)

    def move(self, direction):
        return self.head.move(direction)


class Day9:
    def __init__(self, filename):
        self.filename = filename

    def solve_part1(self):
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
                    pos.add(rope.move(direction))
        return len(pos)


def main():
    day = Day9("input2.txt")
    print("Part 1:", day.solve_part1())
    print("Part 2:", day.solve_part2())


if __name__ == "__main__":
    main()
