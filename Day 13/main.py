from file_loading import load_file_readlines


def contest_search():
    notes_file = "input.txt"
    id_list = []
    delta_t_list = []
    done = False
    step = 1
    time = 1
    pointer = 0

    shuttle_notes = load_file_readlines(notes_file)
    bus_id_list = shuttle_notes[1].split(',')

    for id in range(0, len(bus_id_list)):
        if bus_id_list[id] != 'x':
            id_list.append(int(bus_id_list[id]))
            delta_t_list.append(id)

    while not done:
        if (time + delta_t_list[pointer]) % id_list[pointer] == 0:
            # raise step
            step *= id_list[pointer]

            pointer += 1

            # raise pointer
            if pointer >= len(id_list):
                done = True

        time += step

    print(time)


def calculate_department_time(time, shuttle):
    bus = int(shuttle)
    dt = 0

    last_department = time % bus

    dt = bus - last_department

    return bus, dt


def search_shuttle():
    notes_file = "input.txt"
    department_list = {'line': [], 'department_time': []}

    shuttle_notes = load_file_readlines(notes_file)
    timestamp = int(shuttle_notes[0])
    shuttle_table = shuttle_notes[1].split(',')

    for shuttle in shuttle_table:
        if shuttle != 'x':
            line, department_time = calculate_department_time(timestamp, shuttle)
            department_list['line'].append(line)
            department_list['department_time'].append(department_time)

    print(department_list)


if __name__ == '__main__':
    contest_search()


