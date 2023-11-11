import re


def parse_monkeys() -> dict:
    monkeys = {}
    with open("day11/input11-sample", "rb") as data:
        for line in data:
            line = line.strip().decode("utf8")
            # parse data into structure
            if line.startswith("Monkey"):
                # get monkey number
                key = line.strip().split(" ")
                monkey_num = key[1].replace(":", "")
                monkey = {monkey_num: {}}
            elif "Starting items" in line:
                # parse starting items
                items = list(map(str, re.split('Starting items: | ', line.replace(",", ""))))
                monkey[monkey_num]["items"] = items[1:]
            elif "Operation" in line:
                # parse operation
                ops = line.strip().split(" ")
                monkey[monkey_num]["worry"] = {"op": ops[4], "num": ops[5]}
            elif "Test" in line:
                # parse divisible
                tests = line.strip().split(" ")
                monkey[monkey_num]["test"] = {}
                monkey[monkey_num]["test"]["divisible"] = tests[-1]
                # add to monkey
                pass
            elif "If true" in line:
                # parse true
                tests = line.strip().split(" ")
                monkey[monkey_num]["test"][True] = tests[-1]
            elif "If false" in line:
                # parse false
                tests = line.strip().split(" ")
                monkey[monkey_num]["test"][False] = tests[-1]
                monkeys.update(monkey)
                pass

    return monkeys


def compute_monkey_business(inspections: dict, monkeys: dict, divide_worry: int = 1) -> tuple:
    for key in monkeys.keys():
        while monkeys[key]["items"]:
            # look at an item
            old = int(monkeys[key]["items"][0])
            #print(f"Monkey {key} inspects item {old}")
            # count inspection
            if inspections.get(key):
                inspections[key] += 1
            else:
                inspections[key] = 1
            # compute new worry using op and num
            if monkeys[key]["worry"]["op"] == "*":
                if monkeys[key]["worry"]["num"] == "old":
                    new = old * old
                else:
                    new = old * int(monkeys[key]["worry"]["num"])
            else:
                new = old + int(monkeys[key]["worry"]["num"])
            # print(f"Worry level = {new}")
            # divide worry level by 3
            new_worry = new // divide_worry
            # print(f"Monkey {key} bored so worry level= {new}")
            # remove first item
            monkeys[key]["items"].pop(0)
            if new_worry % int(monkeys[key]["test"]["divisible"]) == 0:
                # append this item to monkey N
                monkeys[monkeys[key]["test"][True]]["items"].append(new)
                # print(f"Current worry level divisible by {monkeys[key]['test']['divisible']}")
                # print(f"Item with worry level {new} thrown to Monkey {monkeys[key]['test'][True]}")
            else:
                # append this item to monkey N
                monkeys[monkeys[key]["test"][False]]["items"].append(new)
                # print(f"Current worry level NOT divisible by {monkeys[key]['test']['divisible']}")
                # print(f"Item with worry level {new} thrown to Monkey {monkeys[key]['test'][False]}")

    return inspections, monkeys


def day11() -> None:
    print("###########")
    print("# Day  11 #")
    print("###########")

    monkeys = parse_monkeys()
    rounds = 20
    inspections = {}
    for i in range(0, rounds):
        results = compute_monkey_business(inspections, monkeys, divide_worry=True)
        inspections = results[0]
        monkeys = results[1]

    # sort
    sorted_dict = sorted(inspections.items(), key=lambda x: x[1], reverse=True)
    print(f"Part 1: Total monkey business is {sorted_dict[0][1]*sorted_dict[1][1]}")

    # monkeys = parse_monkeys()
    # rounds = 10000
    # inspections = {}
    # for i in range(0, rounds):
    #     results = compute_monkey_business(inspections, monkeys)
    #     inspections = results[0]
    #     monkeys = results[1]
    # print("Sorting...")
    # # sort
    # sorted_dict = sorted(inspections.items(), key=lambda x: x[1], reverse=True)
    # print(f"Part 2: Total monkey business is {sorted_dict[0][1]*sorted_dict[1][1]}")


