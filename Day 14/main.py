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


def docking_data():
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


if __name__ == '__main__':
    docking_data()

