from file_loading import load_file_readlines


def change_mask(instruction):
    masks_str = []

    instruction_split = instruction.split(' ')
    mask = instruction_split[2]
    # or mask
    masks_str.append(int(mask.replace('X', '0'), base=2))
    # and mask
    masks_str.append(int(mask.replace('X', '1'), base=2))

    return masks_str

def write_memory(instrucition, mem, masks):
    instruction_split = instrucition.split(' ')
    location = instruction_split[0][4:]
    location = location.replace(']', '')
    value = int(instruction_split[2])

    value = value | masks[0]
    value = value & masks[1]

    mem[location] = value


def docking_data_v1():
    data_file = "input.txt"
    docking_list = load_file_readlines(data_file)
    masks = []
    memory = {}

    for docking_instruction in docking_list:
        if 'mask' in docking_instruction:
            masks = change_mask(docking_instruction)
        if 'mem' in docking_instruction:
            write_memory(docking_instruction, memory, masks)

    print(sum(memory.values()))


def change_mask_v2(instruction):
    x_loc = []
    mask_str = instruction.split()

    for bit in range(0, len(mask_str[2])):
        if mask_str[2][bit] == 'X':
            x_loc.append(len(mask_str[2]) - bit - 1)

    mask_int = int(mask_str[2].replace('X', '0'), base=2)

    return mask_int, x_loc


def calculate_start_location(mask, x_l, location):

    start_loc = int(location) | mask

    for bit in x_l:
        check = 2**bit
        if start_loc & check == check:
            start_loc -= check

    return start_loc


def write_memory_v2(instruction, memory, mask, x_loc):
    instruction_split = instruction.split(' ')
    location = instruction_split[0][4:]
    location = location.replace(']', '')
    value = int(instruction_split[2])

    start_location = calculate_start_location(mask, x_loc, location)

    for bit_counter in range(0, 2**len(x_loc)):
        loc_mask = 1
        offset = 0

        for shifter in range(0, len(x_loc)):
            if bit_counter & loc_mask == loc_mask:
                offset += 2**x_loc[shifter]
            loc_mask = loc_mask << 1

        memory[start_location + offset] = value


def docking_data_v2():
    memory = {}

    data_file = "input.txt"
    docking_list = load_file_readlines(data_file)

    for docking_instruction in docking_list:
        if 'mask' in docking_instruction:
            mask, x_locations = change_mask_v2(docking_instruction)
        if 'mem' in docking_instruction:
            write_memory_v2(docking_instruction, memory, mask, x_locations)

    print(sum(memory.values()))


if __name__ == '__main__':
    docking_data_v2()

