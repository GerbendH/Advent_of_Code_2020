from copy import deepcopy
from file_loading import load_file_readlines



def get_neighbours(fp, row, collum):
    nb = []
    lr = len(fp)
    lc = len(fp[0])

    # top
    if row > 0:
        # left
        if collum > 0:
            nb.append(fp[row - 1][collum - 1])

        # mid
        nb.append(fp[row - 1][collum])

        # right
        if collum + 1 < lc:
            nb.append(fp[row - 1][collum + 1])

    # mid
    # left
    if collum > 0:
        nb.append(fp[row][collum - 1])
    # right
    if collum + 1 < lc:
        nb.append(fp[row][collum + 1])

    # bot
    if row + 1 < lr:
        if collum > 0:
            nb.append(fp[row + 1][collum - 1])

        # mid
        nb.append(fp[row + 1][collum])

        # right
        if collum + 1 < lc:
            nb.append(fp[row + 1][collum + 1])

    return nb

def seating_cycle(fp):
    changes = 0
    neighbours = []
    fp_new = deepcopy(fp)

    for row in range(0, len(fp)):
        for collum in range(0, len(fp[row])):
            if fp[row][collum] != '.':
                neighbours = get_neighbours(fp, row, collum)

                if fp[row][collum] == 'L' and neighbours.count('#') == 0:
                    fp_new[row][collum] = '#'
                    changes += 1

                if fp[row][collum] == '#' and neighbours.count('#') >= 4:
                    fp_new[row][collum] = 'L'
                    changes += 1

    return changes, fp_new

def seating_system():
    floor_plan_file = "input.txt"
    floor_plan_old = []
    cycle = 0
    nb_changes = 1
    seats_taken = 0

    floor_plan = load_file_readlines(floor_plan_file)

    for row in floor_plan:
        floor_plan_old.append(list(row))

    while nb_changes != 0:
        nb_changes, floor_plan_new = seating_cycle(floor_plan_old)
        floor_plan_old = deepcopy(floor_plan_new)
        cycle += 1

    if nb_changes == 0:
        for row in range(0, len(floor_plan_new)):
            for collum in floor_plan_new[row]:
                if collum == '#':
                    seats_taken += 1

    print(seats_taken)


if __name__ == '__main__':
    seating_system()

