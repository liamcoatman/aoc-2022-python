from dataclasses import dataclass

import numpy


TEST_INPUT = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Translation:
    x: int
    y: int


TRANSLATIONS = {
    "U": Translation(0, 1),
    "D": Translation(0, -1),
    "L": Translation(-1, 0),
    "R": Translation(1, 0),
}


def parse_input(input_str: str) -> list[Translation]:
    moves = []
    for line in input_str.strip().splitlines():
        direction, n = line.split()
        for _ in range(int(n)):
            moves.append(TRANSLATIONS[direction])
    return moves


def is_touching(first: Point, second: Point) -> bool:
    return all(
        (
            abs(first.x - second.x) <= 1,
            abs(first.y - second.y) <= 1,
        )
    )


def move_point(point: Point, translation: Translation) -> Point:
    return Point(point.x + translation.x, point.y + translation.y)


def part_1(input_str: str) -> int:
    head_moves = parse_input(input_str)
    head, tail = Point(0, 0), Point(0, 0)
    visited = 1
    for head_move in head_moves:
        head = move_point(head, head_move)
        if is_touching(head, tail):
            continue
        if head.y - tail.y == 0 and abs(head.x - tail.x) == 2:
            tail = move_point(tail, Translation(head.x - tail.x, 0))
        if head.x - tail.x == 0 and abs(head.y - tail.y) == 2:
            tail = move_point(tail, Translation(0, head.y - tail.y))
        if head.x != tail.x and head.y != tail.y:
            tail = move_point(tail, Translation(head.x - tail.x,


            (
        print(head, tail)
        break


def main():
    part_1(TEST_INPUT)


if __name__ == "__main__":
    main()
