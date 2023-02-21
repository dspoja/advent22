from collections import OrderedDict


def list_to_string(location_list: list) -> str:
    return ''.join([str(loc) for loc in location_list])


def day7() -> None:
    print("###########")
    print("# Day  7  #")
    print("###########")

    with open("day7/input7", "rb") as data:
        file_pointer = []
        file_system = {}
        for line in data:
            line = line.strip().decode("utf8")
            if line.startswith("$ cd "):
                # directory change
                _, _, location = line.split(" ")
                if location.replace(" ", "") == "/":
                    # go to root
                    file_pointer = ["/"]
                elif location.replace(" ", "") == "..":
                    # back up one level
                    file_pointer.pop()
                else:
                    # change to location directory
                    file_pointer.append(f"{location.replace(' ', '')}/")
            elif line.startswith("$ ls"):
                # do nothing
                pass
            else:
                # file listing for the last known directory
                if line.startswith("dir"):
                    # create a directory
                    _, dir_name = line.split(" ")
                    file_system[f"{list_to_string(file_pointer)}{dir_name}/"] = 0
                else:
                    # create a file path
                    size, file_name = line.split()
                    file_system[f"{list_to_string(file_pointer)}{file_name}"] = int(size)

    file_system = OrderedDict(sorted(file_system.items()))

    # count directories
    dir_sizes = {}
    for file in file_system.keys():
        path = file[0:file.rfind("/")] + "/"
        if file_system[file] == 0:
            # we have a directory
            dir_sizes[file] = 0
        else:
            # we have a file
            while path.rfind("/") != -1:
                if dir_sizes.get(path):
                    dir_sizes[path] += file_system.get(file, 0)
                else:
                    dir_sizes[path] = file_system.get(file, 0)
                path = path[0:path[0:-1].rfind("/")+1]

    total_sum = 0
    # compute less than 100K directories sum
    for key in dir_sizes.keys():
        if key != "" and dir_sizes[key] < 100000:
            total_sum += dir_sizes[key]

    print(f"Part 1: Total sum of directories under 10k: {total_sum}")

    # part 2
    # Compute which directory is just big enough to free enough space when deleted
    available_space = 70000000 - dir_sizes["/"]
    update_size = 30000000
    minimum = update_size
    needed_space = update_size - available_space
    min_key = ""
    for key in dir_sizes.keys():
        if dir_sizes[key] > needed_space and dir_sizes[key]-needed_space < minimum:
            minimum = dir_sizes[key]-needed_space
            min_key = key
    print(f"Part 2: We need to delete {min_key} to free additional space: {dir_sizes[min_key]}")
