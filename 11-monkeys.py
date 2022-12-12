import re
from collections.abc import Callable
from dataclasses import dataclass
from functools import reduce 
from operator import attrgetter, mul


TEST_INPUT = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""

@dataclass
class Monkey:
    items: list[int]
    operation: Callable[[int], int]
    throw_to: Callable[[int], int]
    divisor: int
    inspected: int = 0

    def get_first_item(self) -> int:
        self.inspected += 1
        return self.operation(self.items.pop(0))

    def throw_to_monkey(self, worry_divisor: int = 1, common_divisor: int = 1) -> tuple[int, int]:
        val = self.get_first_item() // worry_divisor % common_divisor
        return val, self.throw_to(val)


def parse_input(input_: str) -> list[Monkey]:
    monkeys: list[Monkey] = []
    lines = [line for line in reversed(input_.strip().splitlines()) if line]
    while lines:
        lines.pop()
        starting_items = list(map(int, re.findall(r"\d+", lines.pop())))
        operation = eval(f"lambda old: {lines.pop().split(' = ')[1]}")
        [divisor] = re.findall(r"\d+", lines.pop())
        [true_monkey] = re.findall(r"\d+", lines.pop())
        [false_monkey] = re.findall(r"\d+", lines.pop())
        throw_to = eval(f"lambda val: {true_monkey} if val % {divisor} == 0 else {false_monkey}")
        monkeys.append(
            Monkey(
                items=starting_items,
                operation=operation,
                throw_to=throw_to,
                divisor=int(divisor),
            )
        )
    return monkeys


    
def part_1(input_: str) -> int:
    monkeys = parse_input(input_)
    common_divisor = reduce(mul, map(attrgetter("divisor"), monkeys))
    for _ in range(20):
        for monkey in monkeys:
            while monkey.items:
                throw_to_val, throw_to_monkey = monkey.throw_to_monkey(
                    worry_divisor=3,
                    common_divisor=common_divisor,
                )
                monkeys[throw_to_monkey].items.append(throw_to_val)
    return reduce(
        mul, 
        sorted(monkey.inspected for monkey in monkeys)[-2:]
    )
    

def part_2(input_: str) -> int:
    monkeys = parse_input(input_)
    common_divisor = reduce(mul, map(attrgetter("divisor"), monkeys))
    for round in range(10_000):
        for monkey in monkeys:
            while monkey.items:
                throw_to_val, throw_to_monkey = monkey.throw_to_monkey(common_divisor=common_divisor)
                monkeys[throw_to_monkey].items.append(throw_to_val)
    return reduce(
        mul, 
        sorted(monkey.inspected for monkey in monkeys)[-2:]
    )


def main() -> None:
    assert part_1(TEST_INPUT) == 10605
    with open("11-input.txt") as fp:
        print("part 1", part_1(fp.read()))
    assert part_2(TEST_INPUT) == 2713310158
    with open("11-input.txt") as fp:
        print("part 2", part_2(fp.read()))

if __name__ == "__main__":
    main()

