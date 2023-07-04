import math

import numpy as np
from sklearn import tree

from leo_translate.context import Leo_context
from leo_translate.core_module import Int_value
from leo_translate.core_module.control_pod import IfControl, ElseControl
from leo_translate.submodule import Integer, Sign
from leo_translate.utils.utils import table_format_control


def gene_name_and_type(is_negative, feature) -> dict:
    """
    Generate Struct object name_and_type of attributes
    """
    # return: {'node_name': 'u8', 'right': 'u8', 'left': 'u8'}
    res = dict()
    if is_negative:
        for index in range(feature):
            print(f"p{str(index)}", str(Integer.INT32.value))
            res[f"p{str(index)}"] = str(Integer.INT32.value)
    else:
        for index in range(feature):
            res[f"p{str(index)}"] = str(Integer.UINT32.value)

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
                  struct_name, context, is_leaves):
    # get inputs list, use likes {variate}{Sign.POINT.value}{inputs[i]}
    inputs = context.get_struct_by_name(struct_name)
    if inputs:
        inputs = list(inputs.name_and_type.keys())

    def build_tree(head):
        control_tree = []
        # build_tree(head)
        if is_leaves[head]:
            control_tree.append(f"return {values[head]}u32;")
            return control_tree
        nodes_threshold = math.ceil(threshold[head] * fixed_number)
        comp = Sign.LESS_THAN.value if int(threshold[head]) != threshold[head] else Sign.LESS_THAN_OR_EQUAL.value
        left_value = f'{variate}{Sign.POINT.value}{inputs[feature[head]]}'
        right_type = Integer.INT32.value if is_negative else Integer.UINT32.value
        right_value = Int_value(nodes_threshold, right_type).get()
        if_control = IfControl(left_value, right_value, sign=comp,
                               body="\n".join(build_tree(children_left[head]))
                               ).get()
        else_control = ElseControl(body="\n".join(build_tree(children_right[head]))
                                   ).get()
        control_tree += (if_control + else_control).split('\n')
        return control_tree

    body = build_tree(0)
    return body


def dt_to_leo(clf: tree.DecisionTreeClassifier, fixed_number: int, is_negative: bool, leo_name: str = "main"):
    # Get tree information
    children_left, children_right, feature, threshold, values, is_leaves = data_construction(clf)
    # leo context maintain
    leo = Leo_context()
    # Feature inputs as a struct, struct obj as transition inputs
    struct_name = "Inputs"
    name_and_type: dict = gene_name_and_type(is_negative, clf.n_features_in_)
    leo.add_struct(struct_name, name_and_type)
    # transition and body
    variate = 'main'
    u32 = Integer.UINT32.value
    input1 = 'inputs'
    inputs = f"{input1}{Sign.COLON.value} {struct_name}"
    body = generate_body(children_left, children_right, feature, threshold, values, fixed_number, is_negative,
                         input1, struct_name, leo, is_leaves)
    leo.add_transition(variate, inputs, u32, body)

    # leo code generate
    leo_code_list = leo.generate_leo_code_list(leo_name)
    # code table format
    return table_format_control(leo_code_list)
