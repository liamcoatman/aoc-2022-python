TEST_INPUT = """\
30373
25512
65332
33549
35390
"""


def parse_input(input_: str) -> list[list[int]]:
    return [
        [int(item) for item in line]
        for line in input_.strip().splitlines()
    ]


def part_1(input_: str) -> int:
    grid = parse_input(input_)
    viewable = set()

    for row in range(len(grid)):
        max_seen = -float("inf")
        for col in range(len(grid)):
            if grid[row][col] > max_seen:
                viewable.add((row, col))
            max_seen = max(max_seen, grid[row][col])

    for row in range(len(grid)):
        max_seen = -float("inf")
        for col in reversed(range(len(grid))):
            if grid[row][col] > max_seen:
                viewable.add((row, col))
            max_seen = max(max_seen, grid[row][col])

    for col in range(len(grid)):
        max_seen = -float("inf")
        for row in range(len(grid)):
            if grid[row][col] > max_seen:
                viewable.add((row, col))
            max_seen = max(max_seen, grid[row][col])

    for col in range(len(grid)):
        max_seen = -float("inf")
        for row in reversed(range(len(grid))):
            if grid[row][col] > max_seen:
                viewable.add((row, col))
            max_seen = max(max_seen, grid[row][col])

    return len(viewable)


def part_2(input_: str) -> int:
    grid = parse_input(input_)
    scores = []

    for row in range(len(grid)):
        row_scores = []
        for col in range(len(grid)):
            if col == 0:
                left = 0
            else:
                left = 1
                c = col - 1
                while c > 0 and grid[row][c] < grid[row][col]:
                    left += 1
                    c -= 1

            if col == len(grid) - 1:
                right = 0
            else:
                right = 1
                c = col + 1
                while c < len(grid) - 1 and grid[row][c] < grid[row][col]:
                    right += 1
                    c += 1

            if row == 0:
                up = 0
            else:
                up = 1
                r = row - 1
                while r > 0 and grid[r][col] < grid[row][col]:
                    up += 1
                    r -= 1

            if row == len(grid) - 1:
                down = 0
            else:
                down = 1
                r = row + 1
                while r < len(grid) - 1 and grid[r][col] < grid[row][col]:
                    down += 1
                    r += 1

            row_scores.append(up * left * down * right)
        scores.append(row_scores)
    return max(s for score in scores for s in score)


def main():
    assert part_1(TEST_INPUT) == 21
    with open("08-input.txt") as fp:
        print("part 1", part_1(fp.read()))
    assert part_2(TEST_INPUT) == 8
    with open("08-input.txt") as fp:
        print("part 2", part_2(fp.read()))


if __name__ == "__main__":
    main()
