import math

import numpy as np
from sklearn import tree

from leo_translate.context import Leo_context
from leo_translate.core_module import Int_value, ReturnStatement
from leo_translate.core_module.control_pod import IfControl, ElseControl
from leo_translate.submodule import Integer, Sign
from leo_translate.utils.utils import table_format_control, data_control


def gene_name_and_type(is_negative: bool, feature, leo_display_type: str) -> dict:
    """
    Generate Struct object name_and_type of attributes
    """
    # return: {'node_name': 'u8', 'right': 'u8', 'left': 'u8'}
    res = dict()
    if is_negative:
        for index in range(feature):
            print(f"p{str(index)}", leo_display_type)
            res[f"p{str(index)}"] = leo_display_type
    else:
        for index in range(feature):
            res[f"p{str(index)}"] = leo_display_type

    return res


def data_construction(clf: tree.DecisionTreeClassifier):
    # number of nodes
    n_nodes = clf.tree_.node_count
    # Left and right child nodes
    children_left = clf.tree_.children_left
    children_right = clf.tree_.children_right
    # Features: columns of data, element variable names
    feature = clf.tree_.feature
    # threshold: save decision target data, access via tree's children
    threshold = clf.tree_.threshold

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
    return children_left, children_right, feature, threshold, values, is_leaves


def get_next_node():
    return 0


def generate_body(children_left, children_right, feature, threshold, values, fixed_number, is_negative, variate,
                  struct_name, context, is_leaves, leo_display_type, method):
    # get inputs list, use likes {variate}{Sign.POINT.value}{inputs[i]}
    inputs = context.get_struct_by_name(struct_name)
    if inputs:
        inputs = list(inputs.name_and_type.keys())

    def build_tree(head):
        control_tree = []
        # build_tree(head)
        res = ''
        if is_leaves[head]:
            if method == "transition":
                res = ReturnStatement(Int_value(values[head], leo_display_type).get()).get()
                control_tree.append(res)
                return control_tree
            elif method == "function":
                res = ReturnStatement(Int_value(math.ceil(values[head] * fixed_number), leo_display_type).get()).get()
                control_tree.append(res)
                return control_tree
        nodes_threshold = math.ceil(threshold[head] * fixed_number)
        comp = Sign.LESS_THAN.value if int(threshold[head]) != threshold[head] else Sign.LESS_THAN_OR_EQUAL.value
        left_value = f'{variate}{Sign.POINT.value}{inputs[feature[head]]}'
        right_value = Int_value(nodes_threshold, leo_display_type).get()
        if_control = IfControl(left_value, right_value, sign=comp,
                               body="\n".join(build_tree(children_left[head]))
                               ).get()
        else_control = ElseControl(body="\n".join(build_tree(children_right[head]))
                                   ).get()
        control_tree += (if_control + else_control).split('\n')
        return control_tree

    body = build_tree(0)
    return body


def dt_to_leo(clf: tree.DecisionTreeClassifier, dc: data_control, leo_name: str = "main"):
    # Get tree information
    children_left, children_right, feature, threshold, values, is_leaves = data_construction(clf)
    # leo context maintain
    leo = Leo_context()
    # Feature inputs as a struct, struct obj as transition inputs
    struct_name = "Inputs"

    name_and_type: dict = gene_name_and_type(dc.is_negative, clf.n_features_in_, dc.display_type)
    leo.add_struct(struct_name, name_and_type)
    # transition and body
    variate = 'main'
    input1 = 'inputs'
    inputs = f"{input1}{Sign.COLON.value} {struct_name}"
    body = generate_body(children_left, children_right, feature, threshold, values, dc.fixed_number, dc.is_negative,
                         input1, struct_name, leo, is_leaves, dc.display_type, "transition")

    leo.add_transition(variate, inputs, dc.display_type, body)

    # leo code generate
    leo_code_list = leo.generate_leo_code_list(leo_name, dc.fixed_number)
    # code table format
    return table_format_control(leo_code_list)
