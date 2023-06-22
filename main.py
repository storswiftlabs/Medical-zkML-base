# -*- coding: utf-8 -*-
import pandas as pd
import os
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

from decision_tree.dt_to_leo_code import dt_to_leo_code



# def features_list_to_line(features: list):
#     """
#         Feature from list to line format
#         Parameters:
#             features
#         Returns:
#             line in tsv
#     """
#     s = ""
#     for index, ele in enumerate(features):
#         s = s + ele
#         if index != len(features) - 1:
#             s = s + '\t'
#         else:
#             s = s + '\n'
#     return s
#
#
# def feature_two_combine_into_one(feature1, feature2):
#     """
#         Feature_two_combine_into_one
#         Feature two combine into one
#         Parameters:
#             feature1, feature2
#         Returns:
#             mix
#         Mixed type:
#             src type:dst type
#             0 0:0
#             1 0:1
#             0 1:2
#             1 1:3
#     """
#     # print("cc debug feature_two_combine_into_one", feature1, feature2, type(feature1))
#     if feature1 == 'False':
#         if feature2 == 'False':
#             return '0'
#         else:
#             return '2'
#     else:
#         if feature2 == 'False':
#             return '1'
#         else:
#             return '3'
#
#
# def data_preprocess(data_path):
#     with open(data_path, 'r', encoding='Utf-16') as file:
#         last_path = os.path.dirname(data_path)
#         lines = file.readlines()
#         new_path = os.path.join(last_path, "new_data.tsv")
#         with open(new_path, 'w+') as new_file:
#             for line in lines:
#                 line_list = line.replace('\n', '').replace(',', '.').replace('yes', 'True').replace('no', 'False').split('\t')
#                 # get feature, struct new line
#                 last_feature = feature_two_combine_into_one(line_list[-2], line_list[-1])
#                 print(line_list, last_feature)
#                 a = line_list[:len(line_list) - 2]
#                 a.append(last_feature)
#                 new_file.write(features_list_to_line(a))
#         return new_path
#
#
new_path = './data/Chronic_Kidney_Disease/new_data.tsv'
#
# new_path = data_preprocess(data_path)
# with open(data_path, 'r+') as file:
#     file.write(features_list_to_line(feature))
titanic = pd.read_table(new_path, sep="\t", header=None)
print(new_path)
print(titanic)

num_columns = titanic.shape[1]
# The last two fields as perdition args
y = titanic[num_columns-1]
print(y.head())

# The head five fields as training data
x = titanic[[i for i in range(num_columns-1)]]
print("*" * 30 + " x " + "*" * 30)
print(x.head())

# feature extract - One-hot
x_dict_list = x.to_dict(orient='records')
print("*" * 30 + " train_dict " + "*" * 30)
print(pd.Series(x_dict_list[:10]))

dict_vec = DictVectorizer(sparse=False)
x = dict_vec.fit_transform(x_dict_list)
print("*" * 30 + " One-hot " + "*" * 30)
print(x[:5])

# Divide the training set and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Decision tree classifier
dec_tree = DecisionTreeClassifier()
dec_tree.fit(x_train, y_train)
# print("x and y train is：\n", x_train, y_train)

print("*" * 30 + " Decision tree classifier accuracy " + "*" * 30)
print("score", dec_tree.score(x_test, y_test))
dec_tree.predict(x_test)
print("Here are the predictions:", dec_tree.predict(x_test))

# TODO computes the fixed_number in tsv,
#  and the number of digits in the data determines its size,
#  for example (0.1 fixed_number is 10 for 0.12 fixed_number is 100).
# generate leo code, fixed_number by calculate number of decimal places reserved in the input
# leo = dt_to_leo_code(dec_tree, "dt.aleo", fixed_number=10)
# print(leo)
# f = open("autogenerated_dt_model.leo", "w")
# f.write(leo)