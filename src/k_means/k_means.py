# -*- coding: utf-8 -*-
import pandas as pd
import os

from matplotlib import pyplot as plt
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
import numpy as np

# Load dataset
new_path = '../../data/Parkinsons/new_data.tsv'
titanic = pd.read_table(new_path, sep="\t", header=None)

num_columns = titanic.shape[1]
# The last field as perdition args
print(type(titanic[num_columns-1]))
y = titanic[num_columns-1]
print(y.head())

# The head fields as training data
x = titanic[[i for i in range(num_columns-2)]]
print("*" * 30 + " x " + "*" * 30)
print(x.head())

# Feature extract - One-hot
x_dict_list = x.to_dict(orient='records')
print("*" * 30 + " train_dict " + "*" * 30)
print(pd.Series(x_dict_list[:10]))

dict_vec = DictVectorizer(sparse=False)
x = dict_vec.fit_transform(x_dict_list)
print("*" * 30 + " One-hot " + "*" * 30)
print(x[:5])

# Divide the training set and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# Create KMeans object
kMeans = KMeans(init='k-means++', n_clusters=3, n_init=1, random_state=42)
# Train model
# kMeans.fit(x_train, y_train)
kMeans.fit_predict(titanic)

# Score
# print("score", kMeans.score(x_test))
# print("predict result", kMeans.predict(x_test))
# print("Real result", y_test)

# Get k-Means label
labs = kMeans.labels_
print("label_clf", labs)

# Sort the center point coordinates and save them as DataFrame
centers = kMeans.cluster_centers_
print("centers", centers)

# PCA deal with high dimensional data
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(titanic)
data_pca = pca.transform(titanic)
data_pca = pd.DataFrame(data_pca, columns=['PC1', 'PC2'])
data_pca.insert(data_pca.shape[1], 'labels', labs)

# The centers pca reduces the dimensionality of the K-means cluster center,
# corresponding to the two-dimensional coordinate system of the scatter plot
pca = PCA(n_components=2)
pca.fit(centers)
data_pca_centers = pca.transform(centers)
data_pca_centers = pd.DataFrame(data_pca_centers, columns=['PC1', 'PC2'])

# Visualize it:
plt.figure(figsize=(8, 6))
plt.scatter(data_pca.values[:, 0], data_pca.values[:, 1], s=3, c=data_pca.values[:, 2], cmap='Accent')
plt.scatter(data_pca_centers.values[:, 0], data_pca_centers.values[:, 1], marker='o', s=55, c='#8E00FF')
plt.show()
