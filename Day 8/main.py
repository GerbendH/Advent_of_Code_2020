from copy import deepcopy


def load_program(file):
    with open(file) as program_file:
        aoc_program = program_file.readlines()

    for i in range(0, len(aoc_program)):
        aoc_program[i] = aoc_program[i].strip()

    return aoc_program


def handle_instruction(instruction, accumulator, pointer):

    if instruction[0] == 'acc':
        accumulator += int(instruction[1])
        pointer += 1
    elif instruction[0] == 'nop':
        pointer += 1
    elif instruction[0] == 'jmp':
        pointer += int(instruction[1])

    return accumulator, pointer


def run_program(aoc_program):
    accumulator = 0
    program_pointer = 0
    pp_list = []
    program_valid = True

    while program_valid:
        pp_list.append(program_pointer)
        accumulator, program_pointer = handle_instruction(aoc_program[program_pointer], accumulator, program_pointer)

        # check if pointer points to next instruction
        if program_pointer == len(aoc_program):
            program_valid = True
            print(f'accumulator is {accumulator}')

        # out of bounds check
        if not 0 < program_pointer < len(aoc_program):
            program_valid = False

        # check for endless loop
        if program_pointer in pp_list:
            program_valid = False

    return program_valid


def program():
    program_file = "input.txt"

    aoc_program = load_program(program_file)
    aoc_program_original = []

    for instruction in aoc_program:
        aoc_program_original.append(instruction.split())

    for instruction in range(0, len(aoc_program_original)):
        aoc_program_copy = deepcopy(aoc_program_original)

        if aoc_program_copy[instruction][0] != 'acc':
            if aoc_program_copy[instruction][0] == 'jmp':
                aoc_program_copy[instruction][0] = 'nop'
            elif aoc_program_copy[instruction][0] == 'nop':
                aoc_program_copy[instruction][0] = 'jmp'

            if run_program(aoc_program_copy):
                break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    program()
