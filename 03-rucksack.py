import string
from collections.abc import Iterable


TEST_INPUT = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

CHAR_VALUE = {
    char: value for value, char in enumerate(string.ascii_letters, 1)
}


def find_dupicate(rucksack: str) -> str:
    mid = len(rucksack) // 2
    first, second = rucksack[:mid], rucksack[mid:]
    return set(first).intersection(second).pop()


def grouper(rucksacks: list[str]) -> Iterable[list[str]]:
    for i in range(0, len(rucksacks), 3):
        yield rucksacks[i:i + 3]


def part_1(input_: str) -> int:
    return sum(
        CHAR_VALUE[find_dupicate(rucksack)]
        for rucksack in input_.strip().splitlines()
    )


def find_common_element(rucksacks: list[str]) -> str:
    in_common = set(rucksacks[0])
    for rucksack in rucksacks:
        in_common = in_common.intersection(rucksack)
    return in_common.pop()


def part_2(input_: str) -> int:
    return sum(
        CHAR_VALUE[find_common_element(group)]
        for group in grouper(input_.strip().splitlines())
    )


def main():
    assert part_1(TEST_INPUT) == 157
    assert part_2(TEST_INPUT) == 70
    with open("03-input.txt") as fp:
        text = fp.read()
        print("part 1", part_1(text))
        print("part 2", part_2(text))


if __name__ == "__main__":
    main()
