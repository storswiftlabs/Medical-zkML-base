import unittest

import pandas as pd
from sklearn.feature_extraction import DictVectorizer

from XGBoost.xgboost_model import XGBoost_model
from XGBoost.xgboost_to_leo import read_xgb_model
from decision_tree.dt_to_leo_code import quantize_leo


class TestXGBoostMethods(unittest.TestCase):

    def test_main(self):
        # Load dataset
        new_path = '../../data/Acute_Inflammations/new_data.tsv'
        titanic = pd.read_table(new_path, sep="\t", header=None)

        xgb_model = XGBoost_model(titanic)
        num_columns = titanic.shape[1]
        xgb = xgb_model.get_prediction(_len=num_columns - 1)
        fixed_number, is_negative = quantize_leo(titanic.iloc[0])
        read_xgb_model(xgb, fixed_number, is_negative, num_columns - 1)

    def test_data_qua(self):
        """
        generate data by "quantize"
        :return: df data
        """
        new_path = '../../data/Acute_Inflammations/new_data.tsv'
        titanic = pd.read_table(new_path, sep="\t", header=None)
        num_columns = titanic.shape[1]
        # The head five fields as training data
        x = titanic[[i for i in range(num_columns - 1)]]
        print("*" * 30 + " x " + "*" * 30)
        print(x.head())

        dict_vec = DictVectorizer(sparse=False)
        c = dict_vec.fit_transform(x.to_dict(orient="records"))

        import numpy as np
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

if __name__ == '__main__':
    unittest.main()
