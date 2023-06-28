import os.path
import unittest

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction import DictVectorizer

from src.decision_tree.dt_to_leo_code import quantize_leo
from src.k_means.generate_k_means_leo import decimal_significant_digits, generate_main_file
from src.k_means.k_means_model import KMeans_model


class TestKMeansMethods(unittest.TestCase):
    def test_main(self):

        #main_path = "src/k_means/kMeans/src/main.leo"
        paths = os.listdir('data')
        for path in paths:
            # Load dataset
            new_path = os.path.join(os.path.join('data', path), 'new_data.tsv')
            print("path: ", new_path)
            titanic = pd.read_table(new_path, sep="\t", header=None)

            k_Means = KMeans_model(titanic)
            num_columns = titanic.shape[1]
            centers = decimal_significant_digits(k_Means.get_data_cluster(_len=num_columns - 1))
            accuracy, _ = quantize_leo(centers[0])
            leo_path = new_path.replace("\\", "/").split('new_data.tsv')[0]+"k_Means"
            print(leo_path)
            os.makedirs(leo_path, exist_ok=True)
            generate_main_file(centers, accuracy, leo_path+"/main.leo")
            k_Means.get_data_dimensionality_reduction(centers, num_columns)



if __name__ == '__main__':
    unittest.main()
