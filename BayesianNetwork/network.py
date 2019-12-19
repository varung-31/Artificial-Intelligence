# Varun Gupta
# 2016A7PS0087P

from copy import deepcopy


class Node:

    def __init__(self, name, table, parents):
        self.name = name
        self.table = table
        self.parents = parents
        self.parent_positions = None
        self.set_parent_positions()

    def set_parent_positions(self):
        index = 0
        parent_positions = {}
        for parent in self.parents:
            parent_positions[parent] = index
            parent_positions["~" + parent] = index
            index = index + 1
        self.parent_positions = parent_positions


def parse_input_string(string):
    split_values = string.split(" >> ")
    vertex = split_values[0]
    if split_values[1].__len__() != 2:
        parent_list = split_values[1][1:-1].split(",")
    else:
        parent_list = []
    cpt_values = []
    for temp in split_values[2].split(" "):
        cpt_values.append(float(temp))
    return vertex, parent_list, cpt_values


def to_binary(index, counter):
    """ This is a helper function to convert a decimal number "index" into the "counter" number of bits """
    string = '{0:0'
    string = string + str(counter) + 'b}'
    return string.format(index)


def create_bayesian_network(filename):
    file = open(filename, "r")
    bayesian_network = {}
    for line in file:
        if line[0] == "$":
            break
        else:
            vertex, parents, values = parse_input_string(line[:-1])
            # Create binary patterns for indexing within the hash table.
            if not parents:  # parents is empty i.e. vertex is a root node
                ranges = [1]
            else:
                ranges = [x for x in range(0, pow(2, len(parents)))]
            binary_indexes = [to_binary(x, len(parents)) for x in ranges]
            values_dict = {index: value for index, value in zip(binary_indexes, values)}
            node = Node(vertex, values_dict, parents)
            bayesian_network[vertex] = node
            if not parents:
                bayesian_network[vertex].table["0"] = 1 - bayesian_network[vertex].table["1"]
    file.close()
    return bayesian_network


def get_children(bayesian_network, parent):
    ans = []
    for node in bayesian_network:
        if parent in bayesian_network[node].parents:
            ans.append(node)
    return ans


def compute_markov_blanket(bayesian_network, node):
    """ Computes the markov blanket of a given node"""
    ans = set()

    # Get Parents
    parents = bayesian_network[node].parents
    for parent in parents:
        ans.add(parent)

    # Get Children
    children = get_children(bayesian_network, node)
    for child in children:
        ans.add(child)

    # Get Parents of Children
    for child in children:
        parents_of_child = bayesian_network[child].parents
        for parent in parents_of_child:
            ans.add(parent)

    ans.remove(node)
    return ans


def find_encoding(expression, parents, positions):
    parents_encoding = ["0"] * len(parents)
    for parent in parents:
        if parent in expression:
            parents_encoding[positions[parent]] = "1"
        else:
            parents_encoding[positions[parent]] = "0"
    ans = ""
    for element in parents_encoding:
        ans += element
    return ans


def find_parents(expression, parents):
    present_parents = []
    for term in expression:
        if term[0] == "~":  # term is a negative literal
            if term[1] in parents:
                present_parents.append(term)
        else:
            if term[0] in parents:  # term is a positive literal
                present_parents.append(term)
    return present_parents


def find_missing_parents(expression, parents):
    missing_parents = []
    for parent in parents:
        if parent in expression or ('~' + parent) in expression:
            continue
        else:
            missing_parents.append(parent)
    return missing_parents


def get_all_combinations(missing_parents, index, combination):
    if index == len(missing_parents):
        return
    temp = deepcopy(missing_parents)
    temp[index] = '~' + temp[index]
    combination.append(temp)
    get_all_combinations(temp, index + 1, combination)

    temp = deepcopy(missing_parents)
    get_all_combinations(temp, index + 1, combination)


def add_missing_parents(expression, missing_parents):
    expression_list = []
    combination = [missing_parents]
    get_all_combinations(missing_parents, 0, combination)
    for term in combination:
        t = deepcopy(expression)
        t.extend(term)
        expression_list.append(t)
    return expression_list


def recurse_expression(index, expression, bayesian_network):
    if len(expression) == index:
        return 1
    var_consider = expression[index]

    # var_consider is a negative literal
    if var_consider[0] == "~":

        parents_var = bayesian_network[var_consider[1]].parents

        if len(parents_var) == 0:  # no parents
            return bayesian_network[var_consider[1]].table["0"] * recurse_expression(index + 1, expression,
                                                                                     bayesian_network)

        # parents are present
        present_parents = find_parents(expression, parents_var)

        if len(present_parents) == len(parents_var):  # no parents missing
            encoding = find_encoding(present_parents, parents_var, bayesian_network[var_consider[1]].parent_positions)
            prob = 1 - bayesian_network[var_consider[1]].table[encoding]
            return prob * recurse_expression(index + 1, expression, bayesian_network)

        else:  # some parents are missing
            missing_parents = find_missing_parents(expression, parents_var)
            expression_list = add_missing_parents(expression, missing_parents)
            sum = 0
            for exp in expression_list:
                encoding = find_encoding(exp, parents_var, bayesian_network[var_consider[1]].parent_positions)
                prob = 1 - bayesian_network[var_consider[1]].table[encoding]
                sum += prob * recurse_expression(index + 1, exp, bayesian_network)
            return sum

    else:  # var_consider is a positive literal
        parents_var = bayesian_network[var_consider].parents

        if len(parents_var) == 0:  # no parents
            return bayesian_network[var_consider].table["1"] * recurse_expression(index + 1, expression,
                                                                                  bayesian_network)

        # parents are present
        present_parents = find_parents(expression, parents_var)

        if len(present_parents) == len(parents_var):  # no parents missing
            encoding = find_encoding(present_parents, parents_var, bayesian_network[var_consider].parent_positions)
            prob = bayesian_network[var_consider].table[encoding]
            return prob * recurse_expression(index + 1, expression, bayesian_network)

        else:  # some parents are missing
            missing_parents = find_missing_parents(expression, parents_var)
            expression_list = add_missing_parents(expression, missing_parents)
            sum = 0
            for exp in expression_list:
                encoding = find_encoding(exp, parents_var, bayesian_network[var_consider].parent_positions)
                prob = bayesian_network[var_consider].table[encoding]
                sum += prob * recurse_expression(index + 1, exp, bayesian_network)
            return sum


def compute_probability(query_vars, cond_vars, bayesian_network):
    numerator = deepcopy(query_vars)
    numerator.extend(cond_vars)
    numerator_value = recurse_expression(0, numerator, bayesian_network)

    denominator = deepcopy(cond_vars)
    denominator_value = recurse_expression(0, denominator, bayesian_network)

    return float(numerator_value / denominator_value)
