from functools import total_ordering
from typing import Any


TEST_INPUT = """\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


@total_ordering
class Element:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return is_sorted(self.val, other.val)

    def __repr__(self):
        return str(self.val)


def to_pairs(input_: str) -> list[Any]:
    return [
        tuple(map(eval, pair.split("\n"))) 
        for pair in input_.strip().split("\n\n")
    ]


def to_list(input_: str) -> list[Element]:
    return list(
        map(
            Element,
            map(
                eval, 
                filter(
                    lambda x: x, 
                    input_.strip().splitlines()
                )
            )
        )
    )


def is_sorted(left, right) -> bool:
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        if left > right:
            return False
    if isinstance(left, list) and isinstance(right, list):
        if not left:
            return True
        if not right:
            return False
        first = is_sorted(left[0], right[0])
        if first is True:
            return True
        if first is False:
            return False
        return is_sorted(left[1:], right[1:])
    if isinstance(left, list) and isinstance(right, int):
        return is_sorted(left, [right])
    if isinstance(left, int) and isinstance(right, list):
        return is_sorted([left], right)



def part_1(input_: str) -> int:
    return sum(
        i for i, pair in enumerate(to_pairs(input_), 1)
        if is_sorted(*pair)
    )


def part_2(input_: str) -> int:
    items = to_list(input_)
    dividors = [Element([[2]]), Element([[6]])]
    items.extend(dividors)
    items.sort()
    return (items.index(dividors[0]) + 1) * (items.index(dividors[1]) + 1)

def main():
    assert part_1(TEST_INPUT) == 13
    with open("13-input.txt") as fp:
        print("part 1", part_1(fp.read()))
    assert part_2(TEST_INPUT) == 140
    with open("13-input.txt") as fp:
        print("part 2", part_2(fp.read()))

if __name__ == "__main__":
    main()

