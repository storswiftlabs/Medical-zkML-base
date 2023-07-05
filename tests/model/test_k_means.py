import os
import unittest

import pandas as pd

from k_means.k_means_to_leo import generate_k_means_leo_code, centers_fixed_number
from model_generate import KMeansModel
from utils.utils import quantize_leo


class TestKMeansMethods(unittest.TestCase):

    def test_k_means(self):
        # new_path = 'data/Acute_Inflammations/new_data.tsv'
        paths = os.listdir('data')
        for path in paths:
            # Load dataset
            new_path = os.path.join(os.path.join('data', path), 'new_data.tsv')
            print("path: ", new_path)
            titanic = pd.read_table(new_path, sep="\t", header=None)

            k_Means = KMeansModel(titanic)
            print(k_Means)
            num_columns = titanic.shape[1]
            centers = centers_fixed_number(k_Means.get_data_cluster(_len=num_columns - 1))
            print("centers: ", centers)
            # k_Means.get_data_dimensionality_reduction(centers, num_columns)
            accuracy, _ = quantize_leo(centers[0])

            print(''.join(generate_k_means_leo_code(centers, accuracy)))


if __name__ == '__main__':
    unittest.main()
