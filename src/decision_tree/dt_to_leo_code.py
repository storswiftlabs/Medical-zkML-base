import numpy as np
import math
from sklearn import tree
# import pickle


def quantize_leo(line):
    decimal_places = 0
    is_negative = False
    for i in range(0, len(line) - 1):
        if isinstance(line[i], np.int64):
            if line[i] < 0:
                is_negative = True
            continue
        elem = line[i]
        temp = len(np.format_float_positional(elem).split('.')[1])
        
        if np.format_float_positional(elem).split('.')[1] == '':
            if temp < 1:
                temp = 1
        if temp > decimal_places:
            decimal_places = temp
        if elem < 0.0:
            is_negative = True
    return 10 ** decimal_places, is_negative


def dt_to_leo_code(clf: tree.DecisionTreeClassifier, program_name: str, fixed_number: int, is_negative: bool):
    # number of nodes
    n_nodes = clf.tree_.node_count
    # Left and right child nodes
    children_left = clf.tree_.children_left
    children_right = clf.tree_.children_right
    # Features: columns of data, element variable names
    feature = clf.tree_.feature
    # threshold: save decision target data, access via tree's children
    threshold = clf.tree_.threshold

    def generate_dataset_struct(feature, is_negative):
        inputs = []
        inputs.append("\tstruct Inputs {\n")
        if is_negative:
            for index in range(1, feature):
                inputs.append("\t\tp" + str(index) + ":" + " i32,\n")
        else:
            for index in range(1, feature):
                inputs.append("\t\tp" + str(index) + ":" + " u32,\n")
        inputs.append("\t}\n")
        return ''.join(inputs)

    values = [np.argmax(value[0]) for value in clf.tree_.value]
    node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
    is_leaves = np.zeros(shape=n_nodes, dtype=bool)
    stack = [(0, 0)]
    while len(stack) > 0:
        node_id, depth = stack.pop()
        node_depth[node_id] = depth
        is_split_node = children_left[node_id] != children_right[node_id]
        if is_split_node:
            stack.append((children_left[node_id], depth + 1))
            stack.append((children_right[node_id], depth + 1))
        else:
            is_leaves[node_id] = True

    def build_code(i):
        if is_leaves[i]:
            return node_depth[i] * "\t" + f"return {values[i]}u32;\n"
        leo_code = ""
        leo_threshold = math.ceil(threshold[i] * fixed_number)
        comp = "<" if int(threshold[i]) != threshold[i] else "<="
        if is_negative:
            leo_code += node_depth[i] * "\t" + f"if (inputs.p{(feature[i] + 1)} {comp} {leo_threshold}i32) {{\n"
        else:
            leo_code += node_depth[i] * "\t" + f"if (inputs.p{(feature[i] + 1)} {comp} {leo_threshold}u32) {{\n"
        leo_code += build_code(children_left[i])
        leo_code += node_depth[i] * "\t" + "} else {\n"
        leo_code += build_code(children_right[i])
        leo_code += node_depth[i] * "\t" + "}\n"
        return leo_code

    leo_code = f"program {program_name} {{\n"
    leo_code += generate_dataset_struct(clf.n_features_in_ + 1, is_negative)
    if fixed_number >= 10:
        leo_code += "\t" + "// The original data type is float, which increases the precision of data by " + str(fixed_number) + " times.\n"
    leo_code += "\t" + "// Code auto generated from DecisionTreeClassifier using dt_to_leo_code.py. \n"
    leo_code += "\t" + "transition main(inputs: Inputs) -> public u32 {\n"

    node_depth += 2
    leo_code += build_code(0)
    leo_code += "\t}\n}"
    return leo_code
