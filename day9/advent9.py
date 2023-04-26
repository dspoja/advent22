def is_adjacent_y(head: tuple, tail: tuple) -> bool:
    if head[1] == tail[1] or head[1] == tail[1] + 1 or head[1] == tail[1] - 1 or \
            head[1] + 1 == tail[1] or head[1] - 1 == tail[1]:
        return True
    else:
        return False


def is_adjacent(head: tuple, tail: tuple) -> bool:
    if head[0] == tail[0]:
        return is_adjacent_y(head, tail)
    elif head[0] == tail[0] + 1 or head[0] + 1 == tail[0]:
        return is_adjacent_y(head, tail)
    elif head[0] == tail[0] - 1 or head[0] - 1 == tail[0]:
        return is_adjacent_y(head, tail)
    else:
        return False


def part_1() -> None:
    tail_tracker = set()
    tail_tracker.add((0, 0))
    head = (0, 0)
    tail = (0, 0)
    with open("day9/input9", "rb") as data:
        for line in data:
            line = line.strip().decode("utf8")
            direction = line.strip().split(" ")
            spots = int(direction[1])
            for i in range(0, spots):
                if direction[0] == "R":
                    # move head and tail to the right
                    head = (head[0] + 1, head[1])
                    if not is_adjacent(head, tail):
                        tail = (head[0] - 1, head[1])
                        tail_tracker.add(tail)
                elif direction[0] == "L":
                    # move head and tail to the left
                    head = (head[0] - 1, head[1])
                    if not is_adjacent(head, tail):
                        tail = (head[0] + 1, head[1])
                        tail_tracker.add(tail)
                elif direction[0] == "U":
                    # move head and tail up
                    head = (head[0], head[1] + 1)
                    # move tail diagonally up
                    if not is_adjacent(head, tail):
                        if head[0] < tail[0]:
                            # move diagonally up left
                            tail = (tail[0]-1, tail[1]+1)
                        elif head[0] > tail[0]:
                            # move diagonally up right
                            tail = (tail[0]+1, tail[1]+1)
                        else:
                            # move straight up
                            tail = (tail[0], tail[1]+1)
                        tail_tracker.add(tail)
                elif direction[0] == "D":
                    # move head and tail down
                    head = (head[0], head[1] - 1)
                    # move tail diagonally down
                    if not is_adjacent(head, tail):
                        if head[0] < tail[0]:
                            # move diagonally down left
                            tail = (tail[0]-1, tail[1]-1)
                        elif head[0] > tail[0]:
                            # move diagonally down right
                            tail = (tail[0]+1, tail[1]-1)
                        else:
                            # move straight down
                            tail = (tail[0], tail[1]-1)
                        tail_tracker.add(tail)

    print(f"Part 1: Tail tracker has {len(tail_tracker)} visits")


def day9() -> None:
    print("###########")
    print("# Day  9  #")
    print("###########")

    part_1()
