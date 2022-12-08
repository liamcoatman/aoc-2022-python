from __future__ import annotations

from dataclasses import dataclass, field


TEST_INPUT = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    sub_directories: dict[str, Directory] = field(default_factory=dict)
    parent: Directory | None = None
    files: list[File] = field(default_factory=list)

    @property
    def total_file_size(self) -> int:
        return sum(file.size for file in self.files)

    @property
    def total_size(self) -> int:
        return self.total_file_size + sum(
            directory.total_size for directory in self.sub_directories.values()
        )

    @property
    def path(self) -> str:
        if self.parent is None:
            return self.name
        if self.parent.path == "/":
            return "/" + self.name
        return self.parent.path + "/" + self.name


def parse_input(input_: str) -> list[str]:
    return input_.strip().splitlines()


def build_tree(input_: str) -> Directory:
    commands = parse_input(input_)
    root = Directory("/")
    cwd = root
    commands.pop(0)
    while commands:
        command = commands.pop(0)
        if command.split()[1] == "cd":
            target_name = command.split()[2]
            if target_name == "..":
                if cwd.parent is None:
                    continue
                cwd = cwd.parent
            else:
                cwd = cwd.sub_directories[target_name]
        elif command == "$ ls":
            continue
        elif command.split()[0] == "dir":
            name = command.split()[1]
            cwd.sub_directories[name] = Directory(
                name=name,
                parent=cwd,
            )
        else:
            cwd.files.append(
                File(
                    name=command.split()[1],
                    size=int(command.split()[0]),
                )
            )
    return root


def part_1(input_: str) -> int:
    tree = build_tree(input_)

    def dfs(node):
        nonlocal total
        if node.total_size < 100_000:
            total += node.total_size
        for sub_directory in node.sub_directories.values():
            dfs(sub_directory)

    total = 0
    dfs(tree)
    return total


def part_2(input_: str) -> int:
    tree = build_tree(input_)
    disk_size = 70_000_000
    used = tree.total_size
    available = disk_size - used
    required = 30_000_000
    to_free = required - available


    def dfs(node):
        nonlocal smallest
        if node.total_size >= to_free:
            smallest = min(smallest, node.total_size)
        for sub_directory in node.sub_directories.values():
            dfs(sub_directory)

    smallest = float("inf")
    dfs(tree)

    return smallest


def main():
    assert part_1(TEST_INPUT) == 95437
    with open("07-input.txt") as fp:
       print("part 1", part_1(fp.read()))
    assert part_2(TEST_INPUT) == 24933642
    with open("07-input.txt") as fp:
       print("part 2", part_2(fp.read()))

if __name__ == "__main__":
    main()
