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
        centers = kMeans.cluster_centers_
        return centers

    def get_data_dimensionality_reduction(self, centers, _len):
        x = self._get_x_dict(_len)
        y = self._get_y_titanic()
        kMeans = KMeans(init='k-means++', n_clusters=y.nunique(), n_init=1, random_state=42)
        kMeans.fit(x)
        labs = kMeans.predict(x)
        # PCA deal with high dimensional data
        from sklearn.decomposition import PCA
        pca = PCA(n_components=2)
        pca.fit(x)
        data_pca = pca.transform(x)
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
