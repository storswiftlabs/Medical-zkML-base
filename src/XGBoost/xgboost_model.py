from decision_tree.data_analysis import AbcModel
from xgboost import XGBClassifier as XGBC, XGBRegressor as XGBR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE


class XGBoost_model(AbcModel):

    def __init__(self, titanic) -> None:
        """
         Initialize the model. This is called by Titanic to initialize the model. If you don't want to do anything with the model you can call super (). __init__ () # noqa: E501
         @param titanic - A reference to the Titanic object.
         @return True if initialization succeeded False otherwise. Note that a Model is not initialized in this case it will return None # noqa: E501
        """
        super(XGBoost_model, self).__init__(titanic)

    def get_prediction(self, _len):
        """
         Get predictions for a set of data. This is a function to be used in conjunction with : py : meth : ` ~gensim. models. BayesianModel. get_predictions ` # noqa: E501
         @param _len - The length of the
        """
        x = self._get_x_dict(_len)
        y = self._get_y_titanic()
        # Divide the training set and test set
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
        from sklearn.preprocessing import LabelEncoder
        le = LabelEncoder()
        y_train = le.fit_transform(y_train)
        reg = XGBC(n_estimators=10).fit(x_train, y_train)
        reg.predict(x_test)
        print("Score", reg.score(x_test, y_test))
        # Get Mean Square Error
        print("Mean Square Error", MSE(y_test, reg.predict(x_test)))
        # Get feature importance
        print("Feature importance", reg.feature_importances_)
        return reg
