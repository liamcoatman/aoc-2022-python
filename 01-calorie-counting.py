import heapq

TEST_INPUT = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def get_elves(input_: str) -> list[int]:
    return [
        sum(map(int, lines.split()))
        for lines in input_.split("\n\n")
    ]


def part_1(elves: list[int]) -> int:
    return max(elves)


def part_2(elves: list[int]) -> int:
    return sum(heapq.nlargest(3, elves))

if __name__ == "__main__":
    assert part_1(get_elves(TEST_INPUT)) == 24000
    with open("01-input.txt") as fp:
        print(part_1(get_elves(fp.read())))
    assert part_2(get_elves(TEST_INPUT)) == 45000
    with open("01-input.txt") as fp:
        print(part_2(get_elves(fp.read())))
