import pandas as pd
from sklearn import datasets
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# load iris data
iris = datasets.load_iris()
# convert data type to DataFame in padans
labels = pd.DataFrame(iris.target)
labels.columns = ['labels']

data = pd.DataFrame(iris.data)
data.columns = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width']
data = pd.concat([data, labels], axis=1)
print(data.head())

feature = data[['Sepal length', 'Sepal width', 'Petal length', 'Petal width']]
print(feature.head())

# create model and prediction
# using default epsilon = 0.5 and minPoint = 6
model = DBSCAN(min_samples=6)
predict = pd.DataFrame(model.fit_predict(feature))
predict.columns = ['predict']

# concatenate labels to df as a new column
r = pd.concat([feature, predict], axis=1)

# validation of model
ct = pd.crosstab(data['labels'], r['predict'])
print(ct)

# 3D scatter plot
flg = plt.figure(figsize=(6, 6))
ax = Axes3D(flg, rect=[0, 0, .95, 1], elev=48, azim=134)
ax.scatter(r['Sepal length'], r['Sepal length'], r['Petal length'], c=r['predict'], alpha=0.5)
ax.set_xlabel('Sepal length')
ax.set_ylabel('Sepal width')
ax.set_zlabel('Petal length')
plt.show()
