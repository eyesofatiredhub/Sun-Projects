import numpy as np
import pandas as pd
from sklearn.cluster.bicluster import SpectralCoclustering
import matplotlib.pyplot as plt

whisky = pd.read_csv("whiskies.txt")
whisky["Region"] = pd.read_csv("regions.txt")
#print(whisky.iloc[5:10,0:5])
#print(whisky.columns)
flavors = whisky.iloc[:, 2:14]
#print(flavors)
corr_flavors = pd.DataFrame.corr(flavors)
plt.figure(figsize=(10,10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.show()

corr_whisky = pd.DataFrame.corr(flavors.T)
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.axis("tight")
plt.colorbar()
plt.show()

model = SpectralCoclustering(n_clusters = 6, random_state = 0)
model.fit(corr_whisky)
#print(np.sum(model.rows_, axis=1))

whisky["Group"] = pd.Series(model.row_labels_, index = whisky.index)
whisky = whisky._ix[np.argsort(model.row_labels_)]
whisky = whisky.reset_index(drop = True)
correlations = pd.DataFrame.corr(whisky.iloc[:,2:14].T)
correlations = np.array(correlations)
plt.figure(figsize=(10,10))
plt.pcolor(correlations)
plt.axis("tight")
plt.colorbar()
plt.show()

