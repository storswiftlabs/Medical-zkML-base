import pandas as pd
from sklearn.cluster import KMeans

from src.decision_tree.dt_to_leo_code import quantize_leo


def data_cluster(path):
    titanic = pd.read_table(path, sep="\t", header=None)
    num_columns = titanic.shape[1]
    y = titanic[num_columns - 1]
    x = titanic[[i for i in range(num_columns - 1)]]
    kMeans = KMeans(init='k-means++', n_clusters=y.nunique(), n_init=1, random_state=42)
    kMeans.fit(x)
    centers = kMeans.cluster_centers_
    return centers


def generate_main_file(centers, accuracy, path):
    str_list_inputs = []
    str_list_inputs.append("program kMeans.aleo {")
    generate_struct(centers, str_list_inputs)
    generate_transition(centers, accuracy, str_list_inputs)
    str_list_inputs.append("}")
    with open(path, "w+") as file:
        for line in str_list_inputs:
            file.write(line + "\n")


def generate_struct(centers, str_list_inputs):
    temp1 = []
    temp2 = []
    str_list_inputs.append("\tstruct Axis{")
    for index in range(0, len(centers[0])):
        temp1.append("\t\tp" + str(index) + ": i128")
        if index == len(centers[0]) - 1:
            temp1.append("\n\t}\n")
        else:
            temp1.append(",\n")
    str_list_inputs.append(''.join(temp1))

    str_list_inputs.append("\tstruct KMeansCenters {")
    for index in range(0, len(centers)):
        temp2.append("\t\te" + str(index) + ": Axis")
        if index == len(centers) - 1:
            temp2.append("\n\t}\n")
        else:
            temp2.append(",\n")
    str_list_inputs.append(''.join(temp2))


def decimal_significant_digits(centers):
    output = []
    for row in range(len(centers)):
        temp = []
        for col in range(len(centers[row])):
            temp.append(float('%.3g' % centers[row][col]))
        output.append(temp)
    return output


def generate_transition(centers, accuracy, str_list_inputs):
    str_list_inputs.append("\ttransition main(public dataset: Axis) -> i32 {")
    for row in range(len(centers)):
        line = ["\t\tlet point" + str(row) + ": Axis = Axis{"]
        for col in range(len(centers[row])):
            line.append("\n\t\t\tp" + str(col) + ": " + str(int(centers[row][col] * accuracy)) + "i128")
            if col != len(centers[row]) - 1:
                line.append(",")
            else:
                line.append("\n")
        line.append("\t\t};\n")
        str_list_inputs.append(''.join(line))

    for row in range(0, len(centers)):
        for col in range(0, len(centers[row])):
            str_list_inputs.append(
                "\t\tlet point_e" + str(row) + "_p" + str(col) + ": i128 = point" + str(row) + ".p" + str(
                    col) + "-dataset.p" + str(col) + ";")

    for row in range(0, len(centers)):
        line = ["\t\tlet e" + str(row) + ": i128 = "]
        for col in range(0, len(centers[row])):
            line.append("(point_e" + str(row) + "_p" + str(col) + "*" + "point_e" + str(row) + "_p" + str(col) + ")")
            if col != len(centers[row]) - 1:
                line.append("+")
            else:
                line.append(";")
        str_list_inputs.append(''.join(line))

    str_list_inputs.append("\n\t\tlet min_ele_index:i32 = 0i32;")
    for index in range(len(centers) - 1):
        str_list_inputs.append("\t\tif (e" + str(index) + " > e" + str(index + 1) + "){")
        str_list_inputs.append("\t\t\tmin_ele_index = " + str(index + 1) + "i32;")
        str_list_inputs.append("\t\t}else{")
        str_list_inputs.append("\t\t\tmin_ele_index = " + str(index) + "i32;")
        str_list_inputs.append("\t\t}")
    str_list_inputs.append("\t\treturn min_ele_index;")
    str_list_inputs.append("\t}")


# output leo file path
input_path = '../../data/Acute_Inflammations/new_data.tsv'
main_path = "./kMeans/src/main.leo"

# Normal test case from k_means.py
# dataset = [2, 6]  # New point to be predicted
# centers = [[1.167, 1.467], [7.333, 9]]  # Each central point cluster
centers = data_cluster(input_path)
# Generate leo code
# generate_input_file(centers, dataset, input_path)
centers = decimal_significant_digits(centers)
accuracy, _ = quantize_leo(centers[0])
generate_main_file(centers, accuracy, main_path)
