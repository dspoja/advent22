
def get_priority(item: str) -> int:
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38


def day3():
    print("###########")
    print("# Day  3  #")
    print("###########")
    all_most_common = list()
    priority_sum = 0
    lines = list()
    with open("day3/input3", "rb") as data:
        for i, line in enumerate(data):
            lines.append(line.strip().decode("utf8"))

    for line in lines:
        half = int(len(line)/2)
        rucksack1 = line[0:half]
        rucksack2 = line[half:]
        most_common = list()
        for item in rucksack1:
            if item in rucksack2:
                if item not in most_common:
                    most_common.append(item)
        all_most_common.extend(most_common)
    for priority in all_most_common:
        priority_sum += get_priority(priority)
    print(f"Part 1: Total item priority is {priority_sum}")

    triplet_priority = 0
    triplet = list()
    for i, line in enumerate(lines):
        # aggregate 3 rucksacks
        triplet.append(line)
        if (i+1) % 3 == 0:
            # detect most common item
            already_counted = list()
            for item in triplet[0]:
                if item in triplet[1] and item in triplet[2] and item not in already_counted:
                    triplet_priority += get_priority(item)
                    already_counted.append(item)
                    triplet.clear()
                    break

    print(f"Part 2: Total triplet priority is {triplet_priority}")