def find_marker(input_: str, n: int) -> int:
    for i in range(n - 1, len(input_) + 1):
        if len(set(input_[i - n:i])) == n:
            return i


def main():
    assert find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4) == 7
    assert find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 4) == 5
    assert find_marker("nppdvjthqldpwncqszvftbrmjlhg", 4) == 6
    assert find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4) == 10
    assert find_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4) == 11
    with open("06-input.txt") as fp:
        print("part 1", find_marker(fp.read().strip(), 4))
    assert find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
    assert find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
    assert find_marker("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
    assert find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
    assert find_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26
    with open("06-input.txt") as fp:
        print("part 2", find_marker(fp.read().strip(), 14))


if __name__ == "__main__":
    main()
