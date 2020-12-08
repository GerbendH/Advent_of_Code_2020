def get_rules(file):
    with open(file) as rules_file:
        rules = rules_file.readlines()

    for i in range(0, len(rules)):
        rules[i] = rules[i].strip()

    return rules


def rule_interpreter(rule):
    children_rules = []
    children = {}

    # split the rule into different parts
    rule_split = rule.split(',')

    # sort rules out
    parent_rule = rule_split[0]
    for rl_pntr in range(1, len(rule_split)):
        children_rules.append(rule_split[rl_pntr])

    # split further
    parent_rule_split = parent_rule.split()

    # load parent into final form
    parent = parent_rule_split[0] + ' ' + parent_rule_split[1]

    # load children in final form
    if 'no' not in parent_rule_split:
        children[parent_rule_split[-3] + ' ' + parent_rule_split[-2]] = parent_rule_split[-4]

        for child_rule in children_rules:
            child_rule_split = child_rule.split()
            children[child_rule_split[1] + ' ' + child_rule_split[2]] = child_rule_split[0]

    return parent, children


def add_to_tree(tree, parent, children):
    # check if already in tree
    if parent not in tree.keys():
        tree[parent] = {'parents': [], 'children': {} }

    # loop trough children
    for bag_type, number in children.items():
        # add them to a parent when not already there
        if bag_type not in tree[parent]['children'].keys():
            tree[parent]['children'][bag_type] = number

        # add them to tree when not already there
        if bag_type not in tree.keys():
            tree[bag_type] = {'parents': [], 'children': {} }

        if bag_type not in tree[bag_type]['parents']:
            tree[bag_type]['parents'].append(parent)


def count_unique_parents(tree, bag_type):
    all_bags = [bag_type, ]

    for bag in all_bags:
        bag_value = tree.get(bag)

        # check for parent
        if bag_value['parents']:
            for parent in bag_value['parents']:
                if parent not in all_bags:
                    all_bags.append(parent)

    return len(all_bags) - 1


def count_number_children(tree, bag_type):
    bag_instance = 0
    total_bags = 0
    instance_list = []
    bag_list = {}

    # initialise lists with first bag
    instance_list.append(bag_instance)
    bag_list[str(bag_instance)] = [bag_type, 1]

    # run list
    for bag in instance_list:
        for cld_type, cld_count in tree[bag_list[str(bag)][0]]['children'].items():
            # next instance nb
            bag_instance += 1

            # add instance to list
            instance_list.append(bag_instance)

            # add to bag list
            bag_list[str(bag_instance)] = [cld_type, (int(cld_count) * bag_list[str(bag)][1])]

    for instance in bag_list.values():
        total_bags += instance[1]

    return total_bags - 1


def luggage_processing():
    rules_file = "input.txt"
    bag_type_search = 'shiny gold'
    rules_tree = {}

    rules = get_rules(rules_file)

    for rule in rules:
        parent, children = rule_interpreter(rule)
        add_to_tree(rules_tree, parent, children)

    nb_bag_colours = count_unique_parents(rules_tree, bag_type_search)
    nb_children = count_number_children(rules_tree, bag_type_search)

    print(nb_bag_colours)
    print(nb_children)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    luggage_processing()
