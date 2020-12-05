def get_passports(file):
    with open(file) as pp_file:
        pp = pp_file.read()

    return pp


def breakdown_passport_data(pp_data):
    pp_dic = {}
    passport_entries = pp_data.split()

    for entry in passport_entries:
        entry_split = entry.split(':')
        entry_key = entry_split[0].strip()
        entry_value = entry_split[1].strip()
        pp_dic[entry_key] = entry_value

    return pp_dic


def check_year(value, min, max):
    return min <= int(value) <= max


def check_height(value):
    retval = False

    unit = value[-2:]
    height = value[:-2]

    if unit == "in":
        retval = 59 <= int(height) <= 76
    elif unit == "cm":
        retval = 150 <= int(height) <= 193

    return retval

def check_hair(value):
    retval = True
    checklist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

    if len(value) == 7:
        if value[0] == "#":
            for char in range(1, len(value)):
                if value[char] not in checklist:
                    retval = False
        else:
            retval = False
    else:
        retval = False


    return retval


def check_eye(value):
    checklist = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if value in checklist:
        return True
    else:
        return False


def check_passport_id(value):
    if len(value) == 9:
        return True
    else:
        return False


def field_check(field, value):
    fld_check = False

    if field == "byr":
        fld_check = check_year(value, 1920, 2002)
    elif field == "iyr":
        fld_check = check_year(value, 2010, 2020)
    elif field == "eyr":
        fld_check = check_year(value, 2020, 2030)
    elif field == "hgt":
        fld_check = check_height(value)
    elif field == "hcl":
        fld_check = check_hair(value)
    elif field == "ecl":
        fld_check = check_eye(value)
    elif field == "pid":
        fld_check = check_passport_id(value)
    else:
        fld_check = False

    return fld_check


def passport_check(pp, check_fields):
    pp_check = True

    for field in check_fields:
        if field != "cid":

            if field in pp.keys():
                if not field_check(field, pp[field]):
                    pp_check = False
                    break
            else:
                pp_check = False
                break
    return pp_check


def passport_validation():
    passport_file = "input.txt"
    passport_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    valid_passports = 0

    passports_str = get_passports(passport_file)

    passports_list = passports_str.split('\n\n')

    for passport_data in passports_list:
        passport_dic = breakdown_passport_data(passport_data)

        if passport_check(passport_dic, passport_fields):
            valid_passports += 1

    print(valid_passports)


if __name__ == '__main__':
    passport_validation()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
