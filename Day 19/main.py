from copy import deepcopy
from file_loading import load_file_whole

class Rule_class:
    def __init__(self, str, members):
        self.done = False
        self.characters = []
        self.sub_rules = []
        self.children = []
        if str:
            self.characters.append(str)
            self.done = True
        else:
            self.sub_rules = members
            self.children = self.get_children()

    def get_children(self):
        children = []
        for sub_rule in self.sub_rules:
            for rule in sub_rule:
                if rule not in children:
                    children.append(rule)

        return children

    def check_sub_rules(self, rules):
        check = True
        for rule in self.children:
            if not rules[rule].done:
                check = False

        return check

    def create_characters(self, rules):
        test_2 = self.sub_rules
        for sub_rule in self.sub_rules:
            sub_rule_char = []
            new_sub_rule_char = []
            for rule in sub_rule:
                if sub_rule_char:
                    for char in sub_rule_char:
                        for sub_char in rules[rule].characters:
                            new_sub_rule_char.append(char + sub_char)

                    sub_rule_char = deepcopy(new_sub_rule_char)
                else:
                    test = rules[rule].characters
                    sub_rule_char = deepcopy(rules[rule].characters)

            for item in sub_rule_char:
                self.characters.append(item)



def handle_rule(rule, rule_dict):
    rule_split = rule.split(':')
    rule_nb = rule_split[0]
    rule_members = []
    rule_str = ''
    rule_split[1] = rule_split[1].strip()
    if rule_split[1] == '"a"' or rule_split[1] == '"b"':
        rule_str = rule_split[1].replace('"', '')
    else:
        rule_pairs = rule_split[1].split('|')
        for pair in rule_pairs:
            pair_split = pair.split()

            rule_members.append(pair_split)

    rule_dict[rule_nb] = Rule_class(rule_str, rule_members)


def calculate_rules(rules):
    done = False
    while not done:
        done = True
        for rule_nb, rule in rules.items():
            if not rule.done:
                done = False
                if rule.check_sub_rules(rules):
                    rule.create_characters(rules)
                    rule.done = True


def monster_message():
    rule_dict = {}
    image_data_file = "input.txt"
    image_data = load_file_whole(image_data_file)

    image_data_split = image_data.split('\n\n')

    rules = image_data_split[0].split('\n')
    messages = image_data_split[1].split('\n')

    for rule in rules:
        handle_rule(rule, rule_dict)

    calculate_rules(rule_dict)

    print(rule_dict['0'].characters)

    nb_messages = 0

    for message in messages:
        if message in rule_dict['0'].characters:
            nb_messages += 1

    print(nb_messages)


if __name__ == '__main__':
    monster_message()
