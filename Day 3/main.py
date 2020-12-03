def get_map(file):
    with open(file) as map_file:
        map = map_file.readlines()

    for i in range(0, len(map)):
        map[i] = map[i].strip()

    return map


def tree_checker(position):
    if position == '#':
        return True
    else:
        return False


def tree_calculator(step_right, step_down):
    map_file = "input.txt"
    map = get_map(map_file)
    toboggan_position = 0
    tree_counter = 0

    for line in range(0, len(map), step_down):
        # check if toboggan position is in range
        if toboggan_position >= len(map[line]):
            toboggan_position -= len(map[line])

        if tree_checker(map[line][toboggan_position]):
            tree_counter += 1

        toboggan_position += step_right

    return (tree_counter)

def rout_calculator():
    total_trees = []
    answer = 1
    total_trees.append(tree_calculator(1, 1))
    total_trees.append(tree_calculator(3, 1))
    total_trees.append(tree_calculator(5, 1))
    total_trees.append(tree_calculator(7, 1))
    total_trees.append(tree_calculator(1, 2))

    for nb_trees in total_trees:
        answer = answer * nb_trees

    print(answer)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rout_calculator()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
