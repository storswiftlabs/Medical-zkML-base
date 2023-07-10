import os
import unittest

import pandas as pd

from k_means.k_means_to_leo import generate_k_means_leo_code
from leo_translate.utils.utils import data_control
from model_generate import KMeansModel


# def decimal_significant_digits(centers):
#     output = []
#     for row in range(len(centers)):
#         temp = []
#         average = 0
#         for col in range(len(centers[row])):
#             average += centers[row][col]
#         average = average / len(centers[row])
#         if max(centers[row]) / 2 > average:
#             for col in range(len(centers[row])):
#                 temp.append(round(centers[row][col], 2))
#         else:
#             for col in range(len(centers[row])):
#                 temp.append(float('%.3g' % centers[row][col]))
#         output.append(temp)
#     return output


class TestKMeansMethods(unittest.TestCase):

    def test_k_means(self):
        # new_path = 'data/Acute_Inflammations/new_data.tsv'
        paths = os.listdir('data')
        for path in paths:
            # Load dataset
            new_path = os.path.join(os.path.join('data', path), 'new_data.tsv')
            titanic = pd.read_table(new_path, sep="\t", header=None)

            k_Means = KMeansModel(titanic)
            num_columns = titanic.shape[1]
            centers = k_Means.get_data_cluster(_len=num_columns - 1)
            first_line = []
            for index in range(0, len(centers[0])):
                first_line.append(round(centers[0][index], 2))
            dc = data_control(first_line)
            dc.set_leo_display_type('i64')
            k_means = generate_k_means_leo_code(centers, dc, 'kmeans')
            leo_path = "tests/k_means/" + new_path.split("\\")[1] + ".leo"
            with open(leo_path, 'w') as file:
                file.writelines(''.join(k_means))


if __name__ == '__main__':
    unittest.main()
