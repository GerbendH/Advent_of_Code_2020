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

#    for bag, value in all_bags.items():
#        bag_data = tree.get(bag)
#        for bag_data_key, bag_data_value in bag_data['children'].items():
#            all_bags[bag_data_key] = bag_data_value * value

#    print(all_bags)
#    print(tree[bag_type])
#    print(sum(all_bags.values()))

    return 0


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

    # print(nb_bag_colours)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    luggage_processing()
