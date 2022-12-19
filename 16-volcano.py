from __future__ import annotations

import re
from dataclasses import dataclass, field
from collections import deque 


TEST_INPUT = """\
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""


pattern = re.compile(r"Valve ([A-Z][A-Z]) has flow rate=(\d+); tunnels? leads? to valves? (.+)$")


@dataclass 
class Valve:
    name: str 
    rate: int 
    neighbours: list[str]

    @staticmethod
    def from_string(raw: str) -> Valve:
        if match := re.search(pattern, raw):
             name, rate_str, neighbours_str = match.groups()
             return Valve(
                name=name,
                rate=int(rate_str),
                neighbours=neighbours_str.split(", ")
            )
        else:
            raise ValueError(f"Could not parse string {raw}")


@dataclass 
class State:
    position: str
    time: int
    flow: int
    open: set[str]



@dataclass 
class Network:
    valves: list[Valve]
    valves_by_name: dict[str, Valve] = field(init=False)

    def __post_init__(self):
        self.valves_by_name = {valve.name: valve for valve in self.valves}

    def get_valve(self, name: str) -> Valve:
        return self.valves_by_name[name]

    @staticmethod
    def from_string(raw: str) -> Network:
        return Network([Valve.from_string(line) for line in raw.splitlines()])


def part_1(raw: str) -> int:
    network = Network.from_string(raw)
    print(network)


def main() -> None:
    part_1(TEST_INPUT)


if __name__ == "__main__":
    main()

