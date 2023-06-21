from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


class AbcModel(object):

    def __init__(self, titanic):
        """
         Initialize the Titanic object. This is the constructor for the Titanic object. # noqa: E501
         @param titanic - The instance of the Titanic
        """
        self.titanic = titanic

    def _get_x_dict(self, len):
        """
         Get the interception length dictionary from Titanic. This is used to calculate the x_dict
         @param len - the length of the dictionary
         @return dict_vec the dict vectorized to be used in Ruturn the x_dict ( sparse # noqa: E501
        """

        x = self.titanic[[i for i in range(len)]]

        dict_vec = DictVectorizer(sparse=False)
        return dict_vec.fit_transform(x.to_dict(orient="records"))

    def _get_y_titanic(self):
        """
         Get titanic data from a dataframe. This is used to convert the data to a format that can be used by the model. # noqa: E501
         @return DataFrame with columns : y_titanic : 1d array of titanic data
        """
        return self.titanic.iloc[:, -1]


class Model(AbcModel):

    def __init__(self, titanic) -> None:
        """
         Initialize the model. This is called by Titanic to initialize the model. If you don't want to do anything with the model you can call super (). __init__ () # noqa: E501
         @param titanic - A reference to the Titanic object.
         @return True if initialization succeeded False otherwise. Note that a Model is not initialized in this case it will return None # noqa: E501
        """
        super(Model, self).__init__(titanic)

    def get_prediction(self, len):
        """
         Get predictions for a set of data. This is a function to be used in conjunction with : py : meth : ` ~gensim. models. BayesianModel. get_predictions ` # noqa: E501
         @param len - The length of the
        """
        x = self._get_x_dict(len)
        y = self._get_y_titanic()
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.2)  # noqa: E501
        dec_tree = DecisionTreeClassifier().fit(x_train, y_train)
        dec_tree.predict(x_test)
        print("Here are the predictions:", dec_tree.predict(x_test))
        print("score", dec_tree.score(x_test, y_test))
        return dec_tree
