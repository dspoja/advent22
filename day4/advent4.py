import re


def determine_containment(e1_1, e1_2, e2_1, e2_2) -> bool:
    if e1_1 >= e2_1 and e2_1 <= e1_2 <= e2_2:
        return True
    else:
        return False



'''
24-98,24-77
96-98,34-95
29-54,50-53

if 1-1 

'''
def determine_overlap(e1_1, e1_2, e2_1, e2_2) -> bool:
    if e1_1 <= e2_2 and e1_2 >= e2_1:
        print(f"{e1_1}-{e1_2} is overlapping with {e2_1}-{e2_2}")
        return True
    else:
        print(f"{e1_1}-{e1_2} is NOT overlapping with {e2_1}-{e2_2}")
        return False


def day4():
    print("###########")
    print("# Day  4  #")
    print("###########")

    with open("day4/input4", "rb") as data:
        contain_count = 0
        overlap_count = 0
        for line in data:
            line = line.strip().decode("utf8")
            data = list(map(int, re.split(',|-', line)))
            # Part 1
            if determine_containment(data[0], data[1], data[2], data[3]):
                contain_count += 1
            elif determine_containment(data[2], data[3], data[0], data[1]):
                contain_count += 1
            # Part 2
            if determine_overlap(data[0], data[1], data[2], data[3]):
                overlap_count += 1

        print(f"Part 1: There are {contain_count} contained pairs")
        print(f"Part 2: There are {overlap_count} overlapped pairs")
