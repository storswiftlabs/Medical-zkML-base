from xgboost import XGBClassifier as XGBC, XGBRegressor as XGBR

from .leo_transpiler.boostings import XgboostTranspiler

MODEL_NAME = 'XGBoost'


def read_xgb_model(xgb_model: XGBC, save_path, fixed_number: int, is_negative: bool, x_len):
    booster = xgb_model.get_booster()
    features = []
    for i in range(x_len):
        features.append('c' + str(i))
    booster.feature_names = features
    # for i in range(xgb_model.n_estimators):
    #     print("tree_df ", i, ":\n", booster[i].trees_to_dataframe())
    # dt_to_leo_code
    transpiler = XgboostTranspiler(xgb_model, quantize_bits=32)
    transpiler.save_code(save_path, program_name="xgboost")
