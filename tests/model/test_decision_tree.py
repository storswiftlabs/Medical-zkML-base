import os.path
import unittest

import pandas as pd

from leo_translate.utils.utils import data_control
from model_generate import DecisionTreeModel
from src.decision_tree.decision_tree_to_leo import gene_name_and_type, dt_to_leo


class TestDecisionTreeMethods(unittest.TestCase):

    def test_gene_name_and_type(self):
        print(gene_name_and_type(True, 5, 'i32'))
        print(gene_name_and_type(True, 10, 'i32'))

    def test_main(self):
        paths = os.listdir('data')
        for path in paths:
            if path not in ["Acute_Inflammations"]:
                continue
            # Load dataset
            new_path = os.path.join(os.path.join('data', path), 'new_data.tsv')
            print("new_path: ", new_path)
            MODEL_NAME = 'dt'
            titanic = pd.read_table(new_path, sep='\t', header=None)

            dc = data_control(titanic.iloc[0])
            model = DecisionTreeModel(titanic)
            num_columns = titanic.shape[1]
            dec_tree = model.get_prediction(_len=num_columns - 1)

            dt = dt_to_leo(dec_tree, dc, MODEL_NAME)
            leo_path = "tests/dt/" + new_path.split("\\")[1] + ".leo"
            with open(leo_path, 'w+') as file:
                file.writelines(''.join(dt))

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
