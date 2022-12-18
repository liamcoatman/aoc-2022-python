from __future__ import annotations

import re
from collections.abc import Iterator
from dataclasses import dataclass 
from typing import Iterable, TypeAlias

import tqdm

TEST_INPUT = """\
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __lt__(self, other: Point) -> bool:
        if self.x < other.x:
            return True
        elif self.x == other.x:
            return self.y < other.y
        return False


@dataclass
class Sensor:
    position: Point
    beacon: Point

    @property
    def distance_to_beacon(self) -> int:
        return distance(self.position, self.beacon)


Interval: TypeAlias = tuple[int, int]


def distance(first: Point, second: Point) -> int:
    return abs(first.x - second.x) + abs(first.y - second.y)



def parse_input(input_: str) -> Iterator[Sensor]:
    for line in input_.strip().splitlines():
        x1, y1, x2, y2 = map(int, re.findall(r"-?\d+", line))
        yield Sensor(Point(x1, y1), Point(x2, y2))


def unallowable_columns(sensors: Iterable[Sensor], row: int) -> set[int]:
    unallowable_intervals: list[Interval] = []
    for sensor in sensors:

        dist_from_row = abs(sensor.position.y - row)
        remaining = sensor.distance_to_beacon - dist_from_row

        if remaining < 0:
            continue
        else:
            low = sensor.position.x - remaining
            high = sensor.position.x + remaining

            if Point(low, row) == sensor.beacon:
                low += 1
            elif Point(high, row) == sensor.beacon:
                high -= 1

            if low <= high:
                unallowable_intervals.append((low, high))
    
    return set.union(*[set(range(low, high + 1)) for low, high in unallowable_intervals])


def part_1(input_: str, row: int) -> int:
    sensors = parse_input(input_)
    return len(unallowable_columns(sensors, row))


def main():
    assert part_1(TEST_INPUT, 10) == 26
    with open("15-input.txt") as fp:
        print("part 1", part_1(fp.read(), 2000000))


if __name__ == "__main__":
    main()

