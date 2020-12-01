def get_report():

    report_int = []

    report_input_file = open("input.txt", "r")
    if report_input_file.mode == "r":
        report_string = report_input_file.read()
        weight_string_split = report_string.split("\n")

        for weight in weight_string_split:
            report_int.append(int(weight))

    return report_int


def anylysor(report):

    result = 0

    for entry_1 in report:
        for entry_2 in report:
            if entry_1 != entry_2:
                for entry_3 in report:
                    if entry_3 != entry_1 and entry_3 != entry_2:
                        if (entry_1 + entry_2 + entry_3 ) == 2020:
                            result = entry_1 * entry_2 * entry_3
                            print(entry_1)
                            print(entry_2)
                            print(entry_3)
                            print(result)

    return result


def analyse_report():

    report = get_report()
    result = anylysor(report)

    print(result)


if __name__ == '__main__':
    analyse_report()
