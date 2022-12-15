from operator import itemgetter

import numpy

TEST_INPUT = """\
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""


def parse_input(input_: str) -> set[tuple[int, int]]:
    rocks: set[tuple[int, int]] = set()
    for rock in input_.strip().splitlines():
        coords = [tuple(map(int, coord.split(","))) for coord in rock.split(" -> ")]
        for start, end in zip(coords, coords[1:]):
            sign = numpy.sign(end[0] - start[0])
            if sign == 0:
                pass
            else:
                for x in range(start[0], end[0] + sign, sign):
                    rocks.add((x, start[1]))
            sign = numpy.sign(end[1] - start[1])
            if sign == 0:
                pass
            else:
                for y in range(start[1], end[1] + sign, sign):
                    rocks.add((start[0], y))
    return rocks
    


def part_1(input_: str) -> int:
    rocks = parse_input(input_)
    the_abyss = max(rocks, key=itemgetter(1))[1]
    count = 0
    while True:
        x, y = 500, 0
        while True:
            if y == the_abyss:
                print("the abyss!", count)
                import sys; sys.exit()
            if (x, y + 1) not in rocks:
                y += 1 
            elif (x - 1, y + 1) not in rocks:
                y += 1
                x -= 1
            elif (x + 1, y + 1) not in rocks:
                y += 1
                x += 1
            else:
                count += 1
                rocks.add((x, y))
                break


def part_2(input_: str) -> int:
    rocks = parse_input(input_)
    floor = max(rocks, key=itemgetter(1))[1] + 2
    count = 0
    while True:
        x, y = 500, 0
        while True:
            if (x, y + 1) not in rocks and y + 1 != floor:
                y += 1 
            elif (x - 1, y + 1) not in rocks and y + 1 != floor:
                y += 1
                x -= 1
            elif (x + 1, y + 1) not in rocks and y + 1 != floor:
                y += 1
                x += 1
            else:
                count += 1
                if (x, y) == (500, 0):
                    print("blocked", count)
                    import sys; sys.exit()
                rocks.add((x, y))
                break
        print(x, y)




def main():
    # part_1(TEST_INPUT)
    # with open("14-input.txt") as fp:
    #     part_1(fp.read())
    with open("14-input.txt") as fp:
        part_2(fp.read())


if __name__ == "__main__":
    main()

