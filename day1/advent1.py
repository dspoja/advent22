from collections import Counter

import utils


def day1():
    print("###########")
    print("# Day  1  #")
    print("###########")
    calories = utils.read_input_and_get_list_of_lists("day1/input1", skip_new_line=True, get_int=True)
    max_calories = 0
    max_elf = 0
    total_calories = 0
    elf_dict = dict()
    # Figure out which elf brought the most calories
    for i, meals in enumerate(calories):
        for meal in meals:
            total_calories += meal
        if max_calories < total_calories:
            max_calories = total_calories
            max_elf = i
        elf_dict[i + 1] = [total_calories]
        total_calories = 0
    print("* Part 1 *")
    print(f"Elf {max_elf} has the most calories: {max_calories}")
    print("* Part 2 *")
    counter = Counter(elf_dict)
    count = 0
    top_3_total_calories = 0
    # Let the counter do the work of getting us the elves in sorted order
    # by number of calories
    for elf in counter.most_common():
        if count < 3:
            top_3_total_calories += elf[1][0]
            count += 1
        else:
            break
    print(f"Top 3 elves have a total of {top_3_total_calories} calories")



