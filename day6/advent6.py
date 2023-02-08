
def are_different(stream_slice: str) -> bool:
    if len(set(stream_slice)) == len(stream_slice):
        return True
    else:
        return False


def day6():
    print("###########")
    print("# Day  6  #")
    print("###########")

    with open("day6/input6", "rb") as data:
        line = data.readline().strip().decode("utf8")
        # find unique sliding window
        window = 0
        part1_distinct_num = 4
        while window < len(line)-part1_distinct_num:
            if are_different(line[window:part1_distinct_num+window]):
                break
            window += 1
        print(f"Part 1: First start-of-packet marker = {window+part1_distinct_num}")

        part2_distinct_num = 14
        window = 0
        while window < len(line)-part2_distinct_num:
            if are_different(line[window:part2_distinct_num+window]):
                break
            window += 1
        print(f"Part 2: First start-of-message marker = {window+part2_distinct_num}")