def load_program(file):
    with open(file) as program_file:
        aoc_program = program_file.readlines()

    for i in range(0, len(aoc_program)):
        aoc_program[i] = aoc_program[i].strip()

    return aoc_program


def handle_instruction(instruction, accumulator, pointer):

    instruction_split = instruction.split()

    if instruction_split[0] == 'acc':
        accumulator += int(instruction_split[1])
        pointer += 1
    elif instruction_split[0] == 'nop':
        pointer += 1
    elif instruction_split[0] == 'jmp':
        pointer += int(instruction_split[1])

    return accumulator, pointer


def run_program(aoc_program):
    accumulator = 0
    program_pointer = 0
    pp_list = []
    program_valid = True

    while program_valid:
        pp_list.append(program_pointer)
        accumulator, program_pointer = handle_instruction(aoc_program[program_pointer], accumulator, program_pointer)
        if program_pointer in pp_list:
            program_valid = False
            print(f'accumulator is {accumulator}')


def program():
    program_file = "input.txt"

    aoc_program = load_program(program_file)

    run_program(aoc_program)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    program()
