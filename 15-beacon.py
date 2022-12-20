import re
from dataclasses import dataclass
from operator import attrgetter

NUMBER_PATTERN = re.compile(r"-?\d+")

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


@dataclass(frozen=True) 
class Interval:
    start: int
    end: int

    @property
    def size(self) -> int:
        return self.end - self.start + 1 

    def contains(self, val: int) -> bool:
        return self.start <= val <= self.end 


@dataclass
class Sensor:
    position: Point
    beacon: Point

    @property
    def distance_to_beacon(self) -> int:
        return distance(self.position, self.beacon)


def distance(first: Point, second: Point) -> int:
    return abs(first.x - second.x) + abs(first.y - second.y)


def parse_input(input_: str) -> list[Sensor]:
    sensors = []
    for line in input_.strip().splitlines():
        x1, y1, x2, y2 = map(int, NUMBER_PATTERN.findall(line))
        sensors.append(Sensor(Point(x1, y1), Point(x2, y2)))
    return sensors


def blocked_columns(sensor: Sensor, row: int) -> Interval | None:
    x_dist = sensor.distance_to_beacon - abs(sensor.position.y - row)
    left = sensor.position.x - x_dist
    right = sensor.position.x + x_dist
    if left <= right:
        return Interval(left, right)
    return None


def merge_intervals(intervals: list[Interval | None]) -> list[Interval]:
    filtered_intervals = list(filter(None, intervals))
    sorted_intervals = sorted(filtered_intervals, key=attrgetter("start"))
    new_intervals = [sorted_intervals[0]]
    for interval in sorted_intervals[1:]:
        prev = new_intervals[-1]
        if prev.end < interval.start:
            new_intervals.append(interval)
        else:
            new_intervals[-1] = Interval(prev.start, max(prev.end, interval.end))
    return new_intervals


def is_in(val: int, intervals: list[Interval]) -> bool:
    return any(interval.contains(val) for interval in intervals)


def part_1(input_: str, row: int):
    sensors = parse_input(input_)
    sensor_positions = {sensor.position for sensor in sensors}
    beacon_positions = {sensor.beacon for sensor in sensors}
    intervals = [
        blocked_columns(sensor, row) for sensor in sensors
    ]
    intervals = merge_intervals(intervals)
    already_occupied_count = sum(
        is_in(position.x, intervals) for position in sensor_positions if position.y == row
    ) + sum(is_in(position.x, intervals) for position in beacon_positions if position.y == row)
    
    return sum(interval.size for interval in intervals) - already_occupied_count


def main():
    assert part_1(TEST_INPUT, 10) == 26
    with open("15-input.txt") as fp:
        print("part 1", part_1(fp.read(), 2_000_000))


if __name__ == "__main__":
    main()

