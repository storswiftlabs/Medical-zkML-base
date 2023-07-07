import math
import typing as tp

import numpy as np
from xgboost import XGBClassifier as XGBC, XGBRegressor as XGBR

from decision_tree.decision_tree_to_leo import generate_body
from leo_translate.context import Leo_context
from leo_translate.core_module import Int_value, Let, ReturnStatement
from leo_translate.core_module.control_pod import IfControl, ElseControl
from leo_translate.submodule import Integer, Sign
from leo_translate.utils import table_format_control

MODEL_NAME = 'XGBoost'

def get_is_leaves(dfs):
    trees = []
    for df in dfs:
        is_leaves = np.zeros(len(df['Feature']))
        for i, node in enumerate(df.iloc):
            if node['Feature'] == "Leaf":
                is_leaves[i] = 1
        trees.append(is_leaves)
    return trees


def get_threshold(dfs):
    leaf_feature = -2
    trees = []
    for df in dfs:
        classes = []
        for node in df.iloc:
            if node['Feature'] == "Leaf":
                classes.append(leaf_feature)
            else:
                classes.append(node["Split"])
        trees.append(classes)
    return trees


def get_feature(dfs):
    leaf_feature = -2
    trees = []
    for df in dfs:
        classes = []
        for node in df.iloc:
            if node["Feature"] == 'Leaf':
                classes.append(leaf_feature)
            else:
                classes.append(int(node["Feature"].replace('f', '')))
        trees.append(classes)
    return trees


def get_children_left(dfs):
    leaf_children = -1
    trees = []
    for df in dfs:
        classes = []
        for node in df.iloc:
            if node["Feature"] == 'Leaf':
                classes.append(leaf_children)
            else:
                classes.append(int(node["Yes"].split('-')[-1]))
        trees.append(classes)
    return trees


def get_children_right(dfs):
    leaf_children = -1
    trees = []
    for df in dfs:
        classes = []
        for node in df.iloc:
            if node["Feature"] == 'Leaf':
                classes.append(leaf_children)
            else:
                classes.append(int(node["No"].split('-')[-1]))
        trees.append(classes)
    return trees


def get_values(dfs):
    leaf_value = -2
    trees = []
    for df in dfs:
        classes = []
        for node in df.iloc:
            if node["Feature"] != 'Leaf':
                classes.append(leaf_value)
            else:
                classes.append(node["Gain"])
        trees.append(classes)
    return trees


def data_construction(boost, is_classification, struct_name):
    dfs = []
    trees = boost.get_booster()
    n_estimators = boost.n_estimators
    n_classes = 1
    for i in range(n_estimators):
        df = trees[i].trees_to_dataframe()
        if is_classification:
            n_classes = boost.n_classes_
            for c in range(n_classes):
                class_df = df[df["Tree"] == c].reset_index(drop=True)
                if not class_df.empty:
                    dfs.append(class_df)
        else:
            dfs.append(df)
    is_leaves = get_is_leaves(dfs)
    threshold = get_threshold(dfs)
    feature = get_feature(dfs)
    children_left = get_children_left(dfs)
    children_right = get_children_right(dfs)
    values = get_values(dfs)

    return n_estimators, n_classes, is_leaves, threshold, feature, children_left, children_right, values


def generate_functions_body(n_estimators, n_classes, is_leaves_est, threshold_est, feature_est, children_left_est,
                            children_right_est, values_est, fixed_number, struct_name, context):
    """
    description: generate functions_body by trees from xgboost lib
    inputs: origin trees: df[],
    result: [[body,][]] class(body) list in tree list
    """
    is_negative = 1
    functions_body = []
    for i in range(len(is_leaves_est)):
        is_leaves_cls = is_leaves_est[i]
        threshold_cls = threshold_est[i]
        feature_cls = feature_est[i]
        children_left_cls = children_left_est[i]
        children_right_cls = children_right_est[i]
        values_cls = values_est[i]
        sign_function_body = generate_body(children_left_cls, children_right_cls, feature_cls, threshold_cls,
                                           values_cls, fixed_number, is_negative, struct_name.lower(), struct_name,
                                           context, is_leaves_cls)
        functions_body.append(sign_function_body)
    return functions_body


def generate_transition_body(context, first_input_arg, result_type, is_classification, n_classes):
    transition_body = []
    function_list = context.function_list
    let_variate_list = []
    for func in function_list:
        let_variate = func.variate.replace("class", "_class")
        let_variate_list.append(let_variate)
        let_variate_type = Integer.INT32.value
        let_variate_body = f"{func.variate}{Sign.LEFT_PARENTHESIS.value}{first_input_arg}{Sign.RIGHT_PARENTHESIS.value}"
        transition_body.append(Let(let_variate, let_variate_type, let_variate_body).get())
    if not is_classification:
        # for range and add all data
        res_variate = "res"
        res_variate_type = result_type
        res_variate_body = ""
        for index, let_variate in enumerate(let_variate_list):
            res_variate_body += f"{let_variate}"
            if index != len(let_variate_list) - 1:
                res_variate_body += f" {Sign.ADD.value} "
        transition_body.append(Let(res_variate, res_variate_type, res_variate_body).get())
        transition_body.append(ReturnStatement(res_variate).get())
    else:
        i32 = Integer.INT32.value
        res_variate = "res"
        max_ele = "max_ele_index"
        # let: Calculate the sum of the class
        for index in range(n_classes):
            class_list = []
            for let_variate in let_variate_list:
                if f"class{index}" in let_variate:
                    class_list.append(let_variate)
            class_variate_body = ""
            class_variate = "c" + str(index)
            class_variate_type = i32
            for class_index, let_variate in enumerate(class_list):
                class_variate_body += f"{let_variate}"
                if class_index != len(class_list) - 1:
                    class_variate_body += f" {Sign.ADD.value} "
            transition_body.append(Let(class_variate, class_variate_type, class_variate_body).get())
        # if else control: get max res
        transition_body.append(Let(max_ele, i32, "c0").get())
        transition_body.append(Let(res_variate, i32, Int_value(0, i32).get()).get())
        for index in range(1, n_classes):
            left_value = "c" + str(index)
            right_value = max_ele
            sign = Sign.GREATER_THAN.value
            body = f"{max_ele} = {left_value};\n{res_variate} = {str(index)}{i32};"
            transition_body.append(IfControl(left_value, right_value, sign, body).get())
        transition_body.append(ReturnStatement(res_variate).get())
    return transition_body


def xgboost_leo_code(boost, fixed_number: int = 1, is_classification: bool = True, leo_name: str = "main"):
    # Only signed integer types can be used in XGBoost to leo, Because leaf can be negative

    # leo context maintain
    context = Leo_context()
    i32 = Integer.INT32.value
    # Add structs
    struct_name = "Inputs"
    inputs_name_and_type = {}
    for index in range(0, len(boost.feature_importances_)):
        inputs_name_and_type["c" + str(index)] = i32
    context.add_struct(struct_name, inputs_name_and_type)

    # Get xgboost information
    n_estimators, n_classes, is_leaves, threshold, feature, children_left, children_right, values = data_construction(
        boost, is_classification, struct_name)

    # Add functions
    functions_body = generate_functions_body(n_estimators, n_classes, is_leaves, threshold, feature, children_left,
                                             children_right, values, fixed_number, struct_name, context)
    for index, tree in enumerate(functions_body):
        variate = f'trees{int(index / n_classes)}class{index % n_classes}'
        result_type = Integer.INT32.value
        input1 = struct_name.lower()
        inputs = f"{input1}{Sign.COLON.value} {struct_name}"
        context.add_function(variate, inputs, result_type, body=tree)

    # Add transition and body
    variate = 'main'
    result_type = Integer.INT32.value
    input1 = struct_name.lower()
    inputs = f"{input1}{Sign.COLON.value} {struct_name}"
    transition_body = generate_transition_body(context, input1, result_type, is_classification, n_classes)
    context.add_transition(variate, inputs, result_type, transition_body)

    # leo code generate
    leo_code_list = context.generate_leo_code_list(leo_name, fixed_number)
    # code table format
    return table_format_control(leo_code_list)
