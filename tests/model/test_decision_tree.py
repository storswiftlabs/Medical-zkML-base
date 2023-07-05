import os.path
import unittest

import pandas as pd

from model_generate import DecisionTreeModel
from src.decision_tree.decision_tree_to_leo import gene_name_and_type, dt_to_leo
from utils.utils import quantize_leo


class TestDecisionTreeMethods(unittest.TestCase):

    def test_gene_name_and_type(self):
        print(gene_name_and_type(1, 5))
        print(gene_name_and_type(0, 10))

    def test_main(self):
        MODEL_NAME = 'main'
        titanic = pd.read_table("data/Acute_Inflammations/new_data.tsv", sep='\t', header=None)
        fix_number, is_negative = quantize_leo(titanic.iloc[0])
        model = DecisionTreeModel(titanic)
        num_columns = titanic.shape[1]
        dec_tree = model.get_prediction(_len=num_columns - 1)

        dt = dt_to_leo(dec_tree, fix_number, is_negative, MODEL_NAME)
        print("".join(dt))

    def test_export(self):
        import matplotlib.pyplot as plt
        from sklearn.datasets import load_iris
        from sklearn.tree import DecisionTreeClassifier, plot_tree

        from sklearn.tree import export_text

        titanic = pd.read_table("data/Acute_Inflammations/new_data.tsv", sep='\t', header=None)
        model = DecisionTreeModel(titanic)
        num_columns = titanic.shape[1]
        dec_tree = model.get_prediction(_len=num_columns - 1)

        print("children_right", dec_tree.tree_.children_right)
        print("children_left", dec_tree.tree_.children_left)
        print("feature", dec_tree.tree_.feature)
        print("threshold", dec_tree.tree_.threshold)
        r = export_text(dec_tree)
        print(r)


if __name__ == '__main__':
    unittest.main()
