# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from src.decision_tree.data_analysis import AbcModel


class KMeans_model(AbcModel):
    def __init__(self, titanic) -> None:
        """
         Initialize the model. This is called by Titanic to initialize the model. If you don't want to do anything with the model you can call super (). __init__ () # noqa: E501
         @param titanic - A reference to the Titanic object.
         @return True if initialization succeeded False otherwise. Note that a Model is not initialized in this case it will return None # noqa: E501
        """
        super(KMeans_model, self).__init__(titanic)

    def get_data_cluster(self, _len):
        """
            Args:
            titanic: The instance of the Titanic
        Returns:
        """
        x = self._get_x_dict(_len)
        y = self._get_y_titanic()
        kMeans = KMeans(init='k-means++', n_clusters=y.nunique(), n_init=1, random_state=42)
        kMeans.fit(x)
        self.model = kMeans
        centers = kMeans.cluster_centers_
        return centers

    def data_dimensionality_reduction(self, centers, _len):
        x = self._get_x_dict(_len)
        y = self._get_y_titanic()
        # PCA deal with high dimensional data
        from sklearn.decomposition import PCA
        pca = PCA(n_components=2)
        pca.fit(x)
        data_pca = pca.transform(x)
        data_pca = pd.DataFrame(data_pca, columns=['PC1', 'PC2'])
        data_pca.insert(data_pca.shape[1], 'labels', KMeans(init='k-means++', n_clusters=y.nunique(), n_init=1, random_state=42).predict(x))

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

# Load dataset
# new_path = '../../data/Parkinsons/new_data.tsv'
# titanic = pd.read_table(new_path, sep="\t", header=None)
#
#
#
# num_columns = titanic.shape[1]
# # The last field as perdition args
# print(type(titanic[num_columns - 1]))
# y = titanic[num_columns - 1]
# print(y.head())
#
# # The head fields as training data
# x = titanic[[i for i in range(num_columns - 1)]]
# print("*" * 30 + " x " + "*" * 30)
# print(x.head())
#
# # Divide the training set and test set
# # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# # Create KMeans object
# kMeans = KMeans(init='k-means++', n_clusters=y.nunique(), n_init=1, random_state=41)
# # Train model
# kMeans.fit(x)
# # kMeans.fit_predict(titanic)
# # Get k-Means label
# labs = kMeans.predict(x)
# df = pd.DataFrame({'labels': labs, 'y': y})
# print("df", df.values)
# ct = pd.crosstab(df['labels'], df['y'])
# print("ct", ct)
#
# # Visualization↓
#
# # Sort the center point coordinates and save them as DataFrame
# centers = kMeans.cluster_centers_
# print("centers", centers)
#
# # PCA deal with high dimensional data
# from sklearn.decomposition import PCA
# pca = PCA(n_components=2)
# pca.fit(x)
# data_pca = pca.transform(x)
# data_pca = pd.DataFrame(data_pca, columns=['PC1', 'PC2'])
# data_pca.insert(data_pca.shape[1], 'labels', labs)
#
# # The centers pca reduces the dimensionality of the K-means cluster center,
# # corresponding to the two-dimensional coordinate system of the scatter plot
# pca = PCA(n_components=2)
# pca.fit(centers)
# data_pca_centers = pca.transform(centers)
# data_pca_centers = pd.DataFrame(data_pca_centers, columns=['PC1', 'PC2'])
#
# # Visualize it:
# plt.figure(figsize=(8, 6))
# plt.scatter(data_pca.values[:, 0], data_pca.values[:, 1], s=3, c=data_pca.values[:, 2], cmap='Accent')
# plt.scatter(data_pca_centers.values[:, 0], data_pca_centers.values[:, 1], marker='o', s=55, c='#8E00FF')
# plt.show()
