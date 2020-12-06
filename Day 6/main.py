def get_cd_forms(file):
    with open(file) as cdf_file:
        cdf = cdf_file.read()

    return cdf


def count_answers(group_answers):
    checklist = "abcdefghijklmnopqrstuvwxyz"
    count = 0

    group_answers_list = group_answers.split()

    for question in checklist:
        question_check = True

        for individual in group_answers_list:
            if question not in individual:
                question_check = False

        if question_check:
            count += 1

    return count


def handle_cd_forms():
    custom_declarations_file = "input.txt"
    cdf_list_answers = []

    cdf_string = get_cd_forms(custom_declarations_file)

    cdf_list = cdf_string.split('\n\n')

    for group_answers in cdf_list:
        group_answer_count = count_answers(group_answers)
        cdf_list_answers.append(group_answer_count)

    print(sum(cdf_list_answers))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    handle_cd_forms()


