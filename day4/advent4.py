import re


def determine_containment(e1_1, e1_2, e2_1, e2_2) -> bool:
    if e1_1 >= e2_1 and e2_1 <= e1_2 <= e2_2:
        return True
    else:
        return False


def day4():
    print("###########")
    print("# Day  4  #")
    print("###########")

    with open("day4/input4", "rb") as data:
        contain_count = 0
        for line in data:
            line = line.strip().decode("utf8")
            data = list(map(int, re.split(',|-', line)))
            if determine_containment(data[0], data[1], data[2], data[3]):
                contain_count += 1
            elif determine_containment(data[2], data[3], data[0], data[1]):
                contain_count += 1
        print(f"Part 1: There are {contain_count} contained pairs")