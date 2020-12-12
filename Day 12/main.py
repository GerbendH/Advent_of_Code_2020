from file_loading import load_file_readlines


def move_ship(loc, direction, distance):
    # north
    if direction == 0:
        loc[1] += distance
    # east
    elif direction == 90:
        loc[0] += distance
    # south
    elif direction == 180:
        loc[1] -= distance
    # west
    elif direction == 270:
        loc[0] -= distance


def handle_instruction(instruction, location, ship_direction):
    action = instruction[0]
    distance = int(instruction[1:])

    if action == 'F':
        movement_direction = ship_direction
        move_ship(location, movement_direction, distance)
    elif action == 'N':
        movement_direction = 0
        move_ship(location, movement_direction, distance)
    elif action == 'E':
        movement_direction = 90
        move_ship(location, movement_direction, distance)
    elif action == 'S':
        movement_direction = 180
        move_ship(location, movement_direction, distance)
    elif action == 'W':
        movement_direction = 270
        move_ship(location, movement_direction, distance)
    if action == 'R':
        ship_direction += distance
        if ship_direction >= 360:
            ship_direction -= 360
    elif action == 'L':
        ship_direction -= distance
        if ship_direction < 0:
            ship_direction += 360

    return ship_direction


def risk_of_rain():
    instruction_file = "input.txt"
    navigation_instructions = load_file_readlines(instruction_file)
    ship_location = [0, 0]
    ship_direction = 90  # N = 0, E = 90, S = 180, W = 270

    for instruction in navigation_instructions:
        ship_direction = handle_instruction(instruction, ship_location, ship_direction)

    print(abs(ship_location[0] + abs(ship_location[1])))


if __name__ == '__main__':
    risk_of_rain()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
