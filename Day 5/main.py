def get_seats(file):
    with open(file) as map_file:
        seats = map_file.readlines()

    for i in range(0, len(seats)):
        seats[i] = seats[i].strip()

    return seats


def calculate_seat_id(seat):
    id = 0

    for code in seat:
        id = id << 1

        if code == 'B' or code == 'R':
            id += 1

    return id

def get_my_seat(id_list):
    missing_id = 0
    id_start = min(id_list)

    for id in range(1, len(id_list)):
        if id_list[id] - id_list[id - 1] != 1:
            missing_id = id_list[id] - 1

    return missing_id


def boarding():
    seats_file = "input.txt"
    seat_id = []

    seats = get_seats(seats_file)
    for seat in seats:
        seat_id.append(calculate_seat_id(seat))

    print(max(seat_id))

    my_seat_id = get_my_seat(sorted(seat_id))

    print(my_seat_id)


if __name__ == '__main__':
    boarding()


