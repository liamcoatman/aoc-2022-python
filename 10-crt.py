TEST_INPUT = """\
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


def part_1(input_: str) -> int:
    cycle, value, total = 0, 1, 0
    measure_at = {20, 60, 100, 140, 180, 220}
    for line in input_.strip().splitlines():
        cycle += 1
        if cycle in measure_at:
            total += cycle * value
        if line == "noop":
            continue
        cycle += 1
        if cycle in measure_at:
            total += cycle * value
        value += int(line.split()[1])
    return total
   

def part_2(input_: str) -> None:
    sprite = 1 
    cycle = 0
    pixels = []
    for line in input_.strip().splitlines():
        cycle += 1
        if (cycle - 1) % 40 in {sprite - 1, sprite, sprite + 1}:
            pixels.append("#")
        else:
            pixels.append(".")
        print(cycle, sprite, pixels)
        if line == "noop":
            continue 
        cycle += 1
        if (cycle - 1) % 40 in {sprite - 1, sprite, sprite + 1}:
            pixels.append("#")
        else:
            pixels.append(".")
        print(cycle, sprite, pixels)
        sprite += int(line.split()[1])
    for i in range(0, 240, 40):
        print(pixels[i: i + 40])


def main():
    assert part_1(TEST_INPUT) == 13140
    with open("10-input.txt") as fp:
        print("part 1", part_1(fp.read()))
    with open("10-input.txt") as fp:
        part_2(fp.read())


if __name__ == "__main__":
    main()

