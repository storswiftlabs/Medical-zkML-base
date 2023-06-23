from xgboost import XGBRegressor as XGBR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE
import pandas as pd

# Load dataset
new_path = '../../data/Acute_Inflammations/new_data.tsv'
titanic = pd.read_table(new_path, sep="\t", header=None)

num_columns = titanic.shape[1]
# The last field as perdition args
y = titanic[num_columns-1]
print(y.head())

# The head fields as training data
x = titanic[[i for i in range(num_columns-1)]]
print("*" * 30 + " x " + "*" * 30)
print(x.head())

# Divide the training set and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
reg = XGBR(n_estimators=100).fit(x_train, y_train)
reg.predict(x_test)

print("score", reg.score(x_test, y_test))
# Get Mean Square Error
print(MSE(y_test, reg.predict(x_test)))
# Get feature importance
print(reg.feature_importances_)
