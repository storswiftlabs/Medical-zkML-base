from leo_translate.context import Leo_context
from leo_translate.core_module.control_pod import IfControl
from leo_translate.core_module.statement_pod import Let, LetStruct
from leo_translate.submodule import Integer, Sign, AllKeyWords
from leo_translate.utils.utils import table_format_control, data_control


def generate_k_means_leo_code(centers, dc: data_control, leo_name: str = "main"):
    context = Leo_context()
    u32 = Integer.UINT32.value

    transition_name = 'dataset'
    # Abscissa
    abscissa = 'Axis'
    abscissa_fields = {}

    for index in range(0, len(centers[0])):
        abscissa_fields["p" + str(index)] = str(dc.display_type)
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
            values.append(str(int(centers[row][col] * dc.fixed_number)))
        body.append(LetStruct("point" + str(row), context.get_struct_by_name(abscissa), values).get())
        values = []

    for row in range(0, len(centers)):
        for col in range(0, len(centers[row])):
            values.append("(point" + str(row) + ".p" + str(col) + "-" + transition_name + ".p" + str(col) + ")**2u32")
            if col != len(centers[row]) - 1:
                values.append("+")
        body.append(Let("e" + str(row), dc.display_type, ''.join(values)).get())
        values = []

    body.append(Let("min_ele_index", dc.display_type, "e0").get())
    body.append(Let("output", u32, "0u32").get())

    for index in range(1, len(centers)):
        body.append(IfControl("e" + str(index), "min_ele_index", Sign.LESS_THAN.value,
                              "min_ele_index = " + "e" + str(index) + ";\n" + "output = " + str(
                                  index) + u32 + ";").get())

    body.append(AllKeyWords.RETURN.value + " output;")
    # body.append(nest_if_else(len(centers)-1, "min_ele_index", ">"))

    inputs = f"{transition_name}: {abscissa}"
    context.add_transition('main', inputs, u32, body)

    data_arr = context.generate_leo_code_list(leo_name, dc.fixed_number)
    return table_format_control(data_arr)


