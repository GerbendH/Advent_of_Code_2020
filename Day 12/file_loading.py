def load_file_readlines_int(file):
    with open(file) as load_file:
        load_file_list = load_file.readlines()

    for i in range(0, len(load_file_list)):
        load_file_list[i] = int(load_file_list[i].strip())

    return load_file_list

def load_file_readlines(file):
    with open(file) as load_file:
        load_file_list = load_file.readlines()

    for i in range(0, len(load_file_list)):
        load_file_list[i] = load_file_list[i].strip()

    return load_file_list