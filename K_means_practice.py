# K-means practice

from sklearn import metrics
from sklearn.cluster import KMeans, MiniBatchKMeans

import matplotlib.pyplot as plt

import sys

import numpy as np

data = [(2,10),(2,5),(8,4),(5,8),(7,5),(6,4),(1,2),(8,4)]

initial_centroids = [(2,10),(5,8),(1,2)]

"""
np.ndarray(shape=(2,2), dtype=float, order='F')
array([[ -1.13698227e+002,   4.25087011e-303],
       [  2.88528414e-306,   3.27025015e-309]]) 

# class sklearn.cluster.KMeans(n_clusters=8, init='k-means++', n_init=10, max_iter=300,
# tol=0.0001, precompute_distances=True, verbose=0, random_state=None, copy_x=True, n_jobs=1)
"""

km = KMeans(n_clusters=3, init='random', n_init = int(sys.argv[1]))
km.fit(data)

print km.cluster_centers_