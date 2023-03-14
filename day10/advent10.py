PART1_CYCLES = [20, 60, 100, 140, 180, 220]
PART2_CYCLES = [39, 79, 119, 159, 199, 239]


def check_cycle(cycle: int, cycles: list) -> bool:
    if cycle in cycles:
        return True
    return False


def get_pixel_in_sprite(pixel_idx, sprite_start, sprite_end):
    if sprite_start <= pixel_idx <= sprite_end:
        return "#"
    return "."


def part1():
    with open("day10/input10", "rb") as data:
        x = 1
        cycle = 0
        signals = 0
        for line in data:
            line = line.strip().decode("utf8")
            if line.startswith("noop"):
                cycle += 1
                if check_cycle(cycle, PART1_CYCLES):
                    signals += (x * cycle)
            elif line.startswith("add"):
                (_, val) = line.strip().split(" ")
                count = 0
                while count < 2:
                    cycle += 1
                    count += 1
                    if check_cycle(cycle, PART1_CYCLES):
                        signals += (x * cycle)
                x += int(val)
        print(f"Part 1: Signal strength: {signals}")


def part2():
    with open("day10/input10", "rb") as data:
        sprite_middle = 1
        crt = []
        cycle = 0
        crt_line = ""
        for line in data:
            line = line.strip().decode("utf8")
            if line.startswith("noop"):
                crt_line = crt_line + get_pixel_in_sprite(cycle%40, sprite_middle-1, sprite_middle+1)
                if check_cycle(cycle, PART2_CYCLES):
                    crt.append(crt_line)
                    crt_line = ""
                cycle += 1
            elif line.startswith("add"):
                (_, val) = line.strip().split(" ")
                count = 0
                while count < 2:
                    crt_line = crt_line + get_pixel_in_sprite(cycle % 40, sprite_middle - 1, sprite_middle + 1)
                    if check_cycle(cycle, PART2_CYCLES):
                        crt.append(crt_line)
                        crt_line = ""
                    cycle += 1
                    count += 1
                sprite_middle += int(val)
        print("Part 2: CRT")
        for crt_line in crt:
            print(crt_line)


def day10() -> None:
    print("###########")
    print("# Day  10 #")
    print("###########")

    part1()
    part2()
