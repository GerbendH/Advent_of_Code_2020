from file_loading import load_file_readlines

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
    search_shuttle()


