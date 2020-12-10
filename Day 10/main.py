from math import prod
from file_loading import load_file_readlines_int

def joltinator():
    file = "input.txt"
    adapter_list = load_file_readlines_int(file)
    difference_list = []

    section_depth = 0
    section_paths = []
    total_paths = []

    # add 0 for outlet
    adapter_list.append(0)

    internal_adapter_voltage = max(adapter_list) + 3

    # add max + 3 for internal adapter
    adapter_list.append(internal_adapter_voltage)

    adapter_list = sorted(adapter_list)

    for adapter in range(1, len(adapter_list)):
        difference = adapter_list[adapter] - adapter_list[adapter - 1]
        difference_list.append(difference)

    for diff in difference_list:
        if diff == 1:
            section_depth += 1
            if section_depth == 1:
                step_path = 1
                section_paths.append(step_path)
            elif section_depth == 2:
                step_path = section_paths[section_depth - 2] + 1
                section_paths.append(step_path)
            elif section_depth == 3:
                step_path = section_paths[section_depth - 3] + section_paths[section_depth - 2] + 1
                section_paths.append(step_path)
            else:
                step_path = section_paths[section_depth - 4] + section_paths[section_depth - 3] + section_paths[section_depth - 2]
                section_paths.append(step_path)
        else:
            if sum(section_paths) != 0:
                total_paths.append(max(section_paths))
            section_depth = 0
            section_paths = []

    path_counter = 1
    for total in total_paths:
        path_counter = path_counter * total
        print(path_counter)

    print(difference_list)
    print(total_paths)
    print(prod(total_paths))

if __name__ == '__main__':
    joltinator()
