import os.path
import unittest

import pandas as pd
from sklearn.feature_extraction import DictVectorizer

from XGBoost.xgboost_to_leo import xgboost_leo_code
from leo_translate.utils.utils import data_control
from model_generate import XGBoostModel
from utils.utils import quantize_leo


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
            leo_code = xgboost_leo_code(xgb, dc, is_classification, leo_name)
            with open(f"tests/XGBoost/{path}.leo", "w") as f:
                for line in leo_code:
                    f.write(line)

    def test_data_qua(self):
        """
        generate data by "quantize"
        :return: df data
        """
        new_path = 'data/Acute_Inflammations/new_data.tsv'
        titanic = pd.read_table(new_path, sep="\t", header=None)
        num_columns = titanic.shape[1]
        # The head five fields as training data
        x = titanic[[i for i in range(num_columns - 1)]]
        print("*" * 30 + " x " + "*" * 30)
        print(x.head())

        dict_vec = DictVectorizer(sparse=False)
        c = dict_vec.fit_transform(x.to_dict(orient="records"))

        df = pd.DataFrame(c)
        print(df)
        features = []
        for i in range(num_columns - 1):
            features.append(i)
        from XGBoost.leo_transpiler.quantize import quantize
        df[features] = df[features].applymap(lambda x: quantize(x, 32))
        print(df)
        # leo run main "{c0:1163264i32, c1:0i32, c2:32767i32, c3:0i32, c4: 0i32, c5:0i32}"
        # leo run main 1163264i32 0i32 32767i32 0i32 0i32 0i32

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
