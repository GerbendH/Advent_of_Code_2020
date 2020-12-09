def xmas_analyser(number_list, search_number):
    number_check = False

    for number_1 in range(0, len(number_list)):
        for number_2 in range(number_1 + 1, len(number_list)):
            if number_list[number_1] + number_list[number_2] == search_number:
                number_check = True

    return number_check

def xmas_code_breaker(number_list, search_number):

    for step_size in range(2, len(number_list)):
        for pointer in range(step_size, len(number_list)):
            if sum(number_list[pointer - step_size: pointer]) == search_number:
                print(min(number_list[pointer - step_size: pointer]) + max(number_list[pointer - step_size: pointer]))

