import numpy as np
import math
from sklearn import tree
# import pickle


def dt_to_leo_code(clf: tree.DecisionTreeClassifier, program_name: str):
    # number of nodes
    n_nodes = clf.tree_.node_count
    # Left and right child nodes
    children_left = clf.tree_.children_left
    children_right = clf.tree_.children_right
    # Features: columns of data, element variable names
    feature = clf.tree_.feature
    #
    threshold = clf.tree_.threshold

    def generate_dataset_struct(feature):
        inputs = []
        inputs.append("\tstruct Inputs {\n")
        for index in range(1, feature):
            inputs.append("\t\tp"+str(index)+":"+" u32,\n")
        inputs.append("\t}\n")
        return ''.join(inputs)

    values = [np.argmax(value[0]) for value in clf.tree_.value]

    node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
    is_leaves = np.zeros(shape=n_nodes, dtype=bool)
    stack = [(0, 0)]
    while _len(stack) > 0:
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
        leo_threshold = math.ceil(threshold[i])
        comp = "<" if int(threshold[i]) != threshold[i] else "<="
        leo_code += node_depth[i] * "\t" + f"if (inputs.p{(feature[i] + 1)} {comp} {leo_threshold}u32) {{\n"
        leo_code += build_code(children_left[i])
        leo_code += node_depth[i] * "\t" + "} else {\n"
        leo_code += build_code(children_right[i])
        leo_code += node_depth[i] * "\t" + "}\n"
        return leo_code

    leo_code = f"program {program_name} {{\n"
    leo_code += generate_dataset_struct(clf.n_features_in_+1)
    leo_code += "\t" + "// Code auto generated from DecisionTreeClassifier using dt_to_leo_code.py \n"
    leo_code += "\t" + "transition main(inputs: Inputs) -> public u32 {\n"
    # for i in range(1, clf.n_features_in_ + 1):
    #     leo_code += f"p{i}: u32" + (", " if i != clf.n_features_in_ else ") -> public u32 {\n")

    node_depth += 2
    leo_code += build_code(0)
    leo_code += "\t}\n}"
    return leo_code
