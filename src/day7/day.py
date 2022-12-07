
class FS:
    class FSObj:
        def __init__(self, name, size, parent):
            self.name = name
            self._size = size
            self._parent = parent

        def get_size(self):
            return self._size

    class Dir(FSObj):
        def __init__(self, name, path, parent):
            super().__init__(name, 0, parent)
            self.path = path
            self.content = {}

        def add_content(self, obj):
            self.content[obj.name] = obj

        def update_size(self, size):
            self._size += size
            if self._parent is not None:
                self._parent.update_size(size)

        def get_obj(self, path):
            if path == "..":
                return self._parent
            return self.content[path]

        def out(self, prefix):
            res = prefix + f"dir { self.name } | { self._size }\n"
            for child in self.content.values():
                res += prefix + child.out(prefix + "    ")
            return res

        def get_dir_sizes(self):
            res = {self.path: self.get_size()}
            for child in self.content.values():
                if type(child).__name__ == "Dir":
                    res.update(child.get_dir_sizes())
            return res

    class File(FSObj):
        def __init__(self, name, size, parent):
            super().__init__(name, size, parent)
            self._parent.update_size(size)

        def out(self, prefix):
            return prefix + f"{ self.name } | { self._size }\n"

    def __init__(self):
        self._root = FS.Dir("", "/", None)
        self._pwd = self._root

    def cd(self, path):
        if path == "/":
            self._pwd = self._root
        else:
            self._pwd = self._pwd.get_obj(path)

    def add_file(self, name, size):
        self._pwd.add_content(FS.File(name, size, self._pwd))

    def add_dir(self, name):
        path = self._pwd.path + "/" + name
        self._pwd.add_content(FS.Dir(name, path, self._pwd))

    def get_current_obj(self):
        return self._pwd.name

    def print_root(self):
        result = f"PWD: /\n"
        result += self._root.out("")
        print(result)

    def print_pwd(self):
        result = f"PWD: { self.get_current_obj() }\n"
        result += self._pwd.out("")
        print(result)

    def get_dir_sizes(self):
        return self._root.get_dir_sizes()


class Prompt:
    class Command:
        def __init__(self, input_row, output):
            self.command, *self.args = input_row.split('$ ')[1].split(' ')
            self.output = output

        def print(self):
            print(self.command, self.args, self.output)

    def __init__(self, fs):
        self._fs = fs

    def process_input(self, filename):
        with open(filename, "r") as file:
            running_input = None
            running_output = []
            for row in file:
                row = row.strip()
                if row.startswith('$'):
                    if running_input is not None:
                        self._process_command(Prompt.Command(running_input, running_output))
                    running_input = row
                    running_output = []
                else:
                    running_output.append(row)
            self._process_command(Prompt.Command(running_input, running_output))

    def _process_command(self, command):
        if command.command == "cd":
            self._fs.cd(command.args[0])
        elif command.command == "ls":
            for output_line in command.output:
                if output_line.startswith("dir"):
                    self._fs.add_dir(output_line.split("dir ")[1])
                else:
                    size, name = output_line.split(' ')
                    self._fs.add_file(name, int(size))


class Day7:
    def __init__(self, filename):
        self.fs = FS()
        prompt = Prompt(self.fs)
        prompt.process_input(filename)
        self.dir_sizes = self.fs.get_dir_sizes()

    def solve_part1(self):
        return sum(value for value in self.dir_sizes.values() if value < 100000)

    def solve_part2(self):
        needed = 30000000 - 70000000 + self.dir_sizes['/']
        sorted_res = sorted(self.dir_sizes.items(), key=lambda x: x[1])
        for i in sorted_res:
            if i[1] > needed:
                return i[1]


def main():
    day = Day7("input2.txt")
    print(f"Part 1 solution: { day.solve_part1() }")
    print(f"Part 2 solution: {day.solve_part2() }")


if __name__ == "__main__":
    main()
