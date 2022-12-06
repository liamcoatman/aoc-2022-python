from __future__ import annotations

from dataclasses import dataclass


TEST_INPUT = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


@dataclass
class Section:
    start: int
    end: int

    def __lt__(self, other: Section) -> bool:
        return self.start < other.start

    def __eq__(self, other: Section) -> bool:
        return self.start == other.start


@dataclass
class Pair:
    first: Section
    second: Section

    def total_overlap(self) -> bool:
        if self.first == self.second:
            return True
        return self.second.end <= self.first.end

    def partial_overlap(self) -> bool:
        return self.first.end >= self.second.start


def parse_input(input_: str) -> list[Pair]:
    return [
        Pair(
            *sorted(
                Section(*map(int, section.split("-"))) for section in line.split(",")
            )
        )
        for line in input_.strip().splitlines()
    ]


def part_1(input_: str) -> int:
    return sum(pair.total_overlap() for pair in parse_input(input_))


def part_2(input_: str) -> int:
    return sum(pair.partial_overlap() for pair in parse_input(input_))


def main():
    assert part_1(TEST_INPUT) == 2
    assert part_2(TEST_INPUT) == 4
    with open("04-input.txt") as fp:
        text = fp.read()
        print("part 1", part_1(text))
        print("part 2", part_2(text))


if __name__ == "__main__":
    main()
