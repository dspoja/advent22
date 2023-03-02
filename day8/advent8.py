def check_neighbor_trees(
        matrix: list,
        from_pos: int,
        to_pos: int,
        step: int,
        tree: int,
        tree_pos: tuple,
        direction: tuple) -> int:
    visible = False
    row = tree_pos[0] + direction[0]
    column = tree_pos[1] + direction[1]
    for i in range(from_pos, to_pos, step):
        if tree > matrix[row][column]:
            visible = True
        else:
            visible = False
            break
        if direction[0] != 0:
            row += direction[0]
        else:
            column += direction[1]
    return visible


def check_visibility(matrix: list, row: int) -> int:
    tree_count = 0
    for i in range(1, len(matrix[row])-1):
        current = matrix[row][i]
        # check up
        visible = check_neighbor_trees(matrix, row, 0, -1, current, (row, i), (-1, 0))
        if visible:
            tree_count += 1
            continue
        # check down
        visible = check_neighbor_trees(matrix, row, len(matrix)-1, 1, current, (row, i), (1, 0))
        if visible:
            tree_count += 1
            continue
        # check left
        visible = check_neighbor_trees(matrix, i, 0, -1, current, (row, i), (0, -1))
        if visible:
            tree_count += 1
            continue
        # check right
        visible = check_neighbor_trees(matrix, i, len(matrix[row])-1, 1, current, (row, i), (0, 1))
        if visible:
            tree_count += 1

    return tree_count


def day8() -> None:
    print("###########")
    print("# Day  8  #")
    print("###########")

    with open("day8/input8", "rb") as data:
        trees = []
        for line in data:
            line = line.strip().decode("utf8")
            row = [int(height) for height in line]
            trees.append(row)

    # count edge trees
    edges = len(trees[0])*2 + (len(trees)-2)*2

    # check tree heights
    num_trees = edges
    for i in range(1, len(trees)-1):
        num_trees += check_visibility(trees, i)

    print(f"Part 1: Number of visible trees: {num_trees}")
