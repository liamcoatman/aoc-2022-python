TEST_INPUT = """\
A Y
B X
C Z
"""


part_1_score_mapper = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3,
}


part_2_score_mapper = {
    "A X": 3 + 0,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2 + 0,
    "C Y": 3 + 3,
    "C Z": 1 + 6,
}


def parse_input(input_: str) -> list[str]:
    return input_.strip().splitlines()


def part_1(rounds: list[str]) -> int:
    return sum(part_1_score_mapper[round_] for round_ in rounds)


def part_2(rounds: list[str]) -> int:
    return sum(part_2_score_mapper[round_] for round_ in rounds)


def main():
    assert part_1(parse_input(TEST_INPUT)) == 15
    with open("02-input.txt") as fp:
        print(part_1(parse_input(fp.read())))
    assert part_2(parse_input(TEST_INPUT)) == 12
    with open("02-input.txt") as fp:
        print(part_2(parse_input(fp.read())))


if __name__ == "__main__":
    main()
