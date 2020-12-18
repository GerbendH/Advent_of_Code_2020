
def rambunctious_recitation():
    input_numbers = [8, 13, 1, 0, 18, 9]
    turn_storage = {}
    turn = 1

    for number in input_numbers:
        turn_storage[number] = turn
        last_number = number
        turn += 1

    this_turn = 0

    while turn <= 30000000:
        numbers = turn_storage.keys()

        if this_turn in numbers:
            next_turn = turn - turn_storage.get(this_turn)
        else:
            next_turn = 0

        turn_storage[this_turn] = turn

        print(turn)

        if turn == 30000000:
            print(this_turn)

        turn += 1
        this_turn = next_turn


if __name__ == '__main__':
    rambunctious_recitation()

