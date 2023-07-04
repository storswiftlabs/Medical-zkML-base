import os

import pandas as pd

from leo_translate.context import Leo_context
from leo_translate.core_module.control_pod import IfElseControl, IfControl
from leo_translate.core_module.statement_pod import Let, LetStruct
from leo_translate.submodule import Integer, Sign, AllKeyWords
from leo_translate.utils.utils import table_format_control
from src.decision_tree.dt_to_leo_code import quantize_leo
from src.k_means.generate_k_means_leo import decimal_significant_digits
from src.k_means.k_means_model import KMeans_model


def generate_k_means_leo_code(centers, accuracy):
    context = Leo_context()
    i32 = Integer.INT32.value
    u32 = Integer.UINT32.value
    transition_name = 'dataset'
    # Abscissa
    abscissa = 'Axis'
    abscissa_fields = {}

    for index in range(0, len(centers[0])):
        abscissa_fields["p" + str(index)] = str(i32)
    context.add_struct(abscissa, abscissa_fields)

    # Ordinate
    ordinate = 'KMeansCenters'
    ordinate_fields = {}
    for index in range(0, len(centers)):
        ordinate_fields["e" + str(index)] = abscissa
    context.add_struct(ordinate, ordinate_fields)

    body = []
    name_and_type = {}
    values = []
    for row in range(0, len(centers)):
        for col in range(0, len(centers[row])):
            values.append(str(int(centers[row][col] * accuracy)))
        body.append(LetStruct("point" + str(row), context.get_struct_by_name(abscissa), values).get())
        values = []

    for row in range(0, len(centers)):
        for col in range(0, len(centers[row])):
            values.append("(point" + str(row) + ".p" + str(col) + "-" + transition_name + ".p" + str(col) + ")**2u32")
            if col != len(centers[row])-1:
                values.append("+")
        body.append(Let("e" + str(row), i32, ''.join(values)).get())
        values = []

    body.append(Let("min_ele_index", i32, "e0").get())
    body.append(Let("output", u32, "0u32").get())

    for index in range(1, len(centers)):
        body.append(IfControl("e" + str(index), "min_ele_index", Sign.LESS_THAN.value,
                              "min_ele_index = " + "e" + str(index) + ";\n" + "output = " + str(
                                  index) + u32 + ";").get())

    body.append(AllKeyWords.RETURN.value + " output;")
    # body.append(nest_if_else(len(centers)-1, "min_ele_index", ">"))

    inputs = f"{transition_name}: {abscissa}"
    context.add_transition('main', inputs, u32, body)

    data_arr = context.generate_leo_code_list()
    data_arr = table_format_control(data_arr)
    return data_arr



