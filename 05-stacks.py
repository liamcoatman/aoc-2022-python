from collections import defaultdict, deque
from dataclasses import dataclass
import re


TEST_INPUT = """\
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


@dataclass
class Instruction:
    n: int
    from_stack: int
    to_stack: int


def parse_input(input_: str) -> tuple[
    defaultdict[int, deque[str]], list[Instruction]
]:
    stacks: defaultdict[int, deque[str]] = defaultdict(deque)
    instructions: list[Instruction] = []
    for line in input_.rstrip().splitlines():
        if line.startswith("move"):
            instructions.append(
                Instruction(*map(int, re.findall("[0-9]+", line)))
            )
        elif line.lstrip().startswith("1"):
            continue
        else:
            for stack, i in enumerate(range(0, len(line), 4), 1):
                item = line[i:i + 3]
                if item != "   ":
                    stacks[stack].append(item[1])
    return stacks, instructions


def part_1(input_: str) -> str:
    stacks, instructions = parse_input(input_)
    for instruction in instructions:
        for _ in range(instruction.n):
            val = stacks[instruction.from_stack].popleft()
            stacks[instruction.to_stack].appendleft(val)
    return "".join(stacks[key][0] for key in sorted(stacks))


def part_2(input_: str) -> str:
    stacks, instructions = parse_input(input_)
    for instruction in instructions:
        stack = deque([])
        for _ in range(instruction.n):
            val = stacks[instruction.from_stack].popleft()
            stack.append(val)
        while stack:
            stacks[instruction.to_stack].appendleft(stack.pop())
    return "".join(stacks[key][0] for key in sorted(stacks))


def main():
    assert part_1(TEST_INPUT) == "CMZ"
    assert part_2(TEST_INPUT) == "MCD"
    with open("05-input.txt") as fp:
        text = fp.read()
        print("part 1", part_1(text))
        print("part 2", part_2(text))

if __name__ == "__main__":
    main()
