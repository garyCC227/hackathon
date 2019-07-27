import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np; np.random.seed(5)
from sklearn import decomposition, datasets

centers = [[1, 1], [-1, -1], [1, -1]]
iris = datasets.load_iris()
X = iris.data #the floating point values
y = iris.target #unsigned integers specifying group

fig = plt.figure(figsize=(5.5, 3))
ax = Axes3D(fig, rect=[0, 0, .7, 1], elev=48, azim=134)

pca = decomposition.PCA(n_components=3)
pca.fit(X)
X = pca.transform(X)

labelTups = [('Setosa', 0), ('Versicolour', 1), ('Virginica', 2)]
for name, label in labelTups:
    ax.text3D(X[y == label, 0].mean(),
              X[y == label, 1].mean() + 1.5,
              X[y == label, 2].mean(), name,
              horizontalalignment='center',
              bbox=dict(alpha=.5, edgecolor='w', facecolor='w'))
# Reorder the labels to have colors matching the cluster results
y = np.choose(y, [1, 2, 0]).astype(np.float)
sc = ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap="Spectral", edgecolor='k', s=100)

ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])

colors = [sc.cmap(sc.norm(i)) for i in [1, 2, 0]]
custom_lines = [plt.Line2D([],[], ls="", marker='.',
                mec='k', mfc=c, mew=.1, ms=20) for c in colors]
ax.legend(custom_lines, [lt[0] for lt in labelTups],
          loc='center left', bbox_to_anchor=(1.0, .5))

plt.show()
