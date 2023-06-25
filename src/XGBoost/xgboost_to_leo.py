from xgboost import XGBRegressor as XGBR

from decision_tree.dt_to_leo_code import dt_to_leo_code
from leo_transpiler.boostings import XgboostTranspiler

MODEL_NAME = 'XGBoost'


def read_xgb_model(xgb_model: XGBR, fixed_number: int, is_negative: bool, x_len):
    booster = xgb_model.get_booster()
    features = []
    for i in range(x_len):
        features.append('c' + str(i))
    booster.feature_names = features
    # for i in range(xgb_model.n_estimators):
    #     print("tree_df ", i, ":\n", booster[i].trees_to_dataframe())
    # dt_to_leo_code
    print(xgb_model.n_estimators)
    transpiler = XgboostTranspiler(xgb_model, quantize_bits=32)
    transpiler.save_code("./", program_name="xgboost")
