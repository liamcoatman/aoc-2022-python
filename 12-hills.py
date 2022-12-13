from collections import deque


TEST_INPUT = """\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


def parse_input(input_: str) -> list[list[str]]:
    return [list(line) for line in input_.strip().splitlines()]


def to_values(grid: list[list[str]]) -> list[list[int]]:
    return [[ord(node) - ord("a") for node in row] for row in grid]


def find_char(grid: list[list[str]], char: str) -> list[tuple[int, int]]:
    return [
        (row, col)
        for row in range(len(grid))
        for col in range(len(grid[0]))
        if grid[row][col] == char
    ]


def shortest_distance(
    grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]
):
    queue: deque[tuple[tuple[int, int], int]] = deque(((start, 0),))
    shortest_seen = {}

    while queue:
        current, steps = queue.popleft()
        if current == end:
            return steps
        shortest_seen[current] = steps
        next_steps = steps + 1
        x, y = current
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (
                0 <= nx < len(grid)
                and 0 <= ny < len(grid[0])
                and grid[nx][ny] <= grid[x][y] + 1
                and (
                    (nx, ny) not in shortest_seen 
                    or shortest_seen[(nx, ny)] > next_steps
                )
            ):
                shortest_seen[(nx, ny)] = next_steps
                queue.append(((nx, ny), next_steps))
    return 100000


def part_1(input_: str) -> int:
    grid = parse_input(input_)
    [start] = find_char(grid, "S")
    [end] = find_char(grid, "E")
    grid[start[0]][start[1]] = "a"
    grid[end[0]][end[1]] = "z"
    numeric_grid = to_values(grid)
    return shortest_distance(numeric_grid, start, end)


def part_2(input_: str) -> int:
    grid = parse_input(input_)
    [start] = find_char(grid, "S")
    grid[start[0]][start[1]] = "a"
    starts = find_char(grid, "a")
    [end] = find_char(grid, "E")
    grid[end[0]][end[1]] = "z"
    numeric_grid = to_values(grid)
    return min(
        shortest_distance(numeric_grid, start, end)
        for start in starts
    )


def main() -> None:
    assert part_1(TEST_INPUT) == 31
    with open("12-input.txt") as fp:
        print("part 1", part_1(fp.read()))
    assert part_2(TEST_INPUT) == 29, part_2(TEST_INPUT)
    with open("12-input.txt") as fp:
        print("part 2", part_2(fp.read()))


if __name__ == "__main__":
    main()
