import copy
import math
import re


def parse_map_stack(stack: list) -> dict:
    # create crate map
    stacks = stack.pop().split("  ")
    crate_map = {num.replace(" ", ""): [] for num in stacks}
    pos = 0
    for line in stack:
        while pos < len(line):
            if line[pos] not in (" ", "[", "]"):
                crate_map[str(math.ceil(pos/4))].insert(0, line[pos])
            pos += 1
        pos = 1
    return crate_map


def parse_moves(moves: list) -> list:
    directions = []
    for line in moves:
        # move 1 from 2 to 1
        # move 1 crate from stack 2 to stack 1
        replaced = line.replace("move ", "")
        replaced = replaced.replace(" from ", ",")
        replaced = replaced.replace(" to ", ",")
        direction_tuple = tuple(map(int, re.split(',', replaced)))
        directions.append(direction_tuple)
    return directions


def move_crates_9000(crate_map, directions):
    for moves in directions:
        # move 1 crate from stack 2 to stack 1
        for i in range(moves[0]):
            crate_map[str(moves[2])].append(crate_map[str(moves[1])].pop())

    return crate_map


def move_crates_9001(crate_map, directions):
    for (num, from_stack, to_stack) in directions:
        # move 3 crates from stack 1 to stack 3
        crate_map[str(to_stack)].extend(crate_map[str(from_stack)][-num:])
        crate_map[str(from_stack)] = crate_map[str(from_stack)][:-num]

    return crate_map


def day5():
    print("###########")
    print("# Day  5  #")
    print("###########")

    with open("day5/input5", "rb") as data:
        parse_part2 = False
        map_stack = list()
        direction_list = list()
        for line in data:
            line = re.sub('\n', '', line.decode("utf8"))
            if line == "":
                parse_part2 = True
                continue
            # check which line to parse
            if not parse_part2:
                map_stack.append(line)
            else:
                direction_list.append(line)

    crate_map = parse_map_stack(map_stack)
    crate_map_9001 = copy.deepcopy(crate_map)
    directions = parse_moves(direction_list)
    crate_map_9000 = move_crates_9000(crate_map, directions)
    print("Part 1:")
    for key in crate_map_9000.keys():
        print(f"{crate_map_9000[key].pop()}")

    crate_map_9001 = move_crates_9001(crate_map_9001, directions)
    print("Part 2:")
    for key in crate_map_9001.keys():
        print(f"{crate_map_9001[key].pop()}")