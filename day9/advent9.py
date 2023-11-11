def is_adjacent_y(head: tuple, tail: tuple) -> bool:
    x_adjacent = False
    y_adjacent = False
    if head[0] == tail[0] or head[0] == tail[0]+1 or head[0] == tail[0]-1 or \
            head[0]+1 == tail[0] or head[0]-1 == tail[0]:
        x_adjacent = True

    if head[1] == tail[1] or head[1] == tail[1]+1 or head[1] == tail[1]-1 or \
            head[1]+1 == tail[1] or head[1]-1 == tail[1]:
        y_adjacent = True

    return x_adjacent and y_adjacent


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
                head, tail = move_cycle(direction, head, tail)
                tail_tracker.add(tail)

    print(f"Part 1: Tail tracker has {len(tail_tracker)} visits")


def move_cycle(direction: list, head: tuple, tail: tuple, move_head=True) -> tuple:
    if direction[0] == "R":
        # move head and tail to the right
        if move_head:
            head = (head[0] + 1, head[1])
        if not is_adjacent(head, tail):
            if head[1] > tail[1]:
                tail = (tail[0] + 1, tail[1] + 1)
            elif head[1] < tail[1]:
                tail = (tail[0] + 1, tail[1] -1)
            else:
                tail = (tail[0] + 1, tail[1])
    elif direction[0] == "L":
        # move head and tail to the left
        if move_head:
            head = (head[0] - 1, head[1])
        if not is_adjacent(head, tail):
            if head[1] < tail[1]:
                tail = (tail[0] - 1, tail[1] - 1)
            elif head[1] > tail[1]:
                tail = (tail[0] - 1, tail[1] + 1)
            else:
                tail = (tail[0] - 1, tail[1])
    elif direction[0] == "U":
        # move head and tail up
        if move_head:
            head = (head[0], head[1] + 1)
        # move tail diagonally up
        if not is_adjacent(head, tail):
            if head[0] < tail[0]:
                # move diagonally up left
                tail = (tail[0] - 1, tail[1] + 1)
            elif head[0] > tail[0]:
                # move diagonally up right
                tail = (tail[0] + 1, tail[1] + 1)
            else:
                # move straight up
                tail = (tail[0], tail[1] + 1)
    elif direction[0] == "D":
        # move head and tail down
        if move_head:
            head = (head[0], head[1] - 1)
        # move tail diagonally down
        if not is_adjacent(head, tail):
            if head[0] < tail[0]:
                # move diagonally down left
                tail = (tail[0] - 1, tail[1] - 1)
            elif head[0] > tail[0]:
                # move diagonally down right
                tail = (tail[0] + 1, tail[1] - 1)
            else:
                # move straight down
                tail = (tail[0], tail[1] - 1)

    return head, tail


def part_2() -> None:
    tail_tracker = set()
    tail_tracker.add((0, 0))
    knots = [(0, 0) for _ in range(10)]
    with open("day9/input9-sample", "rb") as data:
        for line in data:
            line = line.strip().decode("utf8")
            direction = line.strip().split(" ")
            spots = int(direction[1])
            print(f"Walking {line}")
            for i in range(1, spots+1):
                first_time = True
                for j in range(0, i%9):
                    current = knots[j]
                    if first_time:
                        current, new_knot_pos = move_cycle(direction, current, knots[j+1])
                        knots[0] = current
                        knots[1] = new_knot_pos
                        first_time = False
                    elif not is_adjacent_y(current, knots[j+1]):
                        current, new_knot_pos = move_cycle(direction, current, knots[j+1], False)
                        knots[j+1] = new_knot_pos

                    if j == 9:
                        tail_tracker.add(current)
                print(f"Knots:{knots}")

    print(f"Part 2: Tail tracker has {len(tail_tracker)} visits")
    print(f"Tail tracker has {tail_tracker} visits")

'''
R4
Move head
Move knot 1

Move head
Move knot 1 and 2

Move head
Move knot 1 and 2 and 3

Move head
Move knot 1 and 2 and 3 and 4
Check the rest of the knots are adjacent and move if needed

break

U4
Move head
Move knot 1
'''

def day9() -> None:
    print("###########")
    print("# Day  9  #")
    print("###########")

    # part_1()
    part_2()
