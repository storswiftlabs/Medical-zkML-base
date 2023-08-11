import os.path
import unittest

import pandas as pd
from sklearn.feature_extraction import DictVectorizer

from src.XGBoost.xgboost_to_leo import xgboost_leo_code
from leo_translate.utils.utils import data_control
from model_generate import XGBoostModel


class TestXGBoostMethods(unittest.TestCase):

    def test_xgboost(self):
        """
        Generate leo code of all dataset
        read dataset -> train -> model to leo code
        """
        leo_name = "xgboost"
        model_type = "classification"
        is_classification = False
        if model_type == "classification":
            is_classification = True
        paths = os.listdir('data')
        for path in paths:
            if path not in ["Chronic_Kidney_Disease"]:
                continue
            # Load dataset
            new_path = os.path.join(os.path.join('data', path), 'new_data.tsv')
            print(new_path)
            titanic = pd.read_table(new_path, sep="\t", header=None)
            # init model_generate
            xgb_model = XGBoostModel(titanic)
            num_columns = titanic.shape[1]
            # model_generate training
            xgb = xgb_model.get_prediction(data_len=num_columns - 1, model_type=model_type)
            dc = data_control(titanic.iloc[0])
            dc.set_leo_display_type('i32')
            dc.set_fixed_number(10)
            leo_code = xgboost_leo_code(xgb, dc, is_classification, leo_name)
            with open(f"tests/XGBoost/{path}.leo", "w") as f:
                for line in leo_code:
                    f.write(line)

    def test_export(self):
        titanic = pd.read_table("data/Acute_Inflammations/new_data.tsv", sep='\t', header=None)
        # init model_generate
        xgb_model = XGBoostModel(titanic)
        num_columns = titanic.shape[1]
        model_type = "classification"
        xgb = xgb_model.get_prediction(data_len=num_columns - 1, model_type=model_type)
        trees = xgb.get_booster()

        print("n_classes_", xgb.n_classes_)
        print("n_estimators", xgb.n_estimators)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        for tree in trees:
            print("trees_to_dataframe()", tree.trees_to_dataframe())


if __name__ == '__main__':
    unittest.main()
