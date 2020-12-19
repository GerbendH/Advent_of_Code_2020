import re
from file_loading import load_file_whole


def get_field_rules(td):
    rules = {}

    td_split = td.split('\n')

    for rule in td_split:
        name = re.match(r'([\w\s]+):', rule).group(1)
        rules[name] = []
        for low, high in re.findall(r'(\d+)-(\d+)', rule):
            rules[name].append([int(low), int(high)])

    return rules

def check_nb_ticket(ticket, rules):
    error = 0
    ticket_valid = True

    for field in ticket:
        for rule in rules.values():
            valid = False
            if rule[0][0] <= int(field) <= rule[0][1] or rule[1][0] <= int(field) <= rule[1][1]:
                valid = True

        if not valid:
            error += int(field)
            ticket_valid = False

    ticket.append(ticket_valid)

    return error


def ticket_translation():
    ticket_file = "input.txt"
    error_rate = 0
    field_lookup = {}

    ticket_data = load_file_whole(ticket_file)
    ticket_data_split = ticket_data.split('\n\n')

    field_rules = get_field_rules(ticket_data_split[0])
    own_ticket = ticket_data_split[1].split('\n')
    nearby_tickets = ticket_data_split[2].split('\n')

    own_ticket.__delitem__(0)
    nearby_tickets.__delitem__(0)

    own_ticket = own_ticket[0].split(',')

    for nb_ticket in range(len(nearby_tickets)):
        nearby_tickets[nb_ticket] = nearby_tickets[nb_ticket].split(',')
        error_rate += check_nb_ticket(nearby_tickets[nb_ticket], field_rules)

    for f_name, f_rule in field_rules.items():
        for field in range(len(nearby_tickets[0])):
            column_check = True
            for ticket in range(len(nearby_tickets)):
                if nearby_tickets[ticket][-1]:
                    check = int(nearby_tickets[ticket][field])
                    if not (f_rule[0][0] <= check <= f_rule[0][1]) and not(f_rule[1][0] <= check <= f_rule[1][1]):
                        column_check = False

            if column_check:
                if f_name in field_lookup.keys():
                    field_lookup[f_name].append(field)
                else:
                    field_lookup[f_name] = [field]

    done = False
    del_values = []
    while not done:
        done = True
        for search_field in field_lookup.values():
            if len(search_field) == 1 and search_field[0] not in del_values:
                del_value = search_field[0]
                del_values.append(del_value)
                done = False
                for del_field in field_lookup.values():
                    if len(del_field) != 1 and del_value in del_field:
                        del_field.remove(del_value)

    answer = 1

    for field, location in field_lookup.items():
        if field.startswith('departure'):
            answer *= int(own_ticket[location[0]])

    print(error_rate)
    print(answer)


if __name__ == '__main__':
    ticket_translation()


