
def read_input_and_get_list_of_lists(file_name: str, skip_new_line=False, get_int=False) -> list:
    # read in input data
    list_of_lists = list()
    with open(file_name, "rb") as data:
        list_of_items = list()
        for line in data:
            line = line.strip().decode("utf8")
            if skip_new_line and not line:
                list_of_lists.append(list_of_items)
                list_of_items = list()
                continue
            if line and get_int:
                line = int(line)
            list_of_items.append(line)
    if list_of_items:
        list_of_lists.append(list_of_items)
    return list_of_lists
