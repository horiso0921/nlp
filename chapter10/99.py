from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

import numpy as np


def _99():
    matries = np.empty([0, 300], dtype=np.float64)
    countries = []
    with open("96") as target:
        for line in target:
            word, matrix = line.strip().split("\t")
            matrix = np.array(list(map(np.float64, matrix.split())))
            matries = np.vstack([matries, matrix])
            countries.append(word)

        t_sne = TSNE().fit_transform(matries)

        predicts = KMeans(n_clusters=5).fit_predict(matries)

        fig, ax = plt.subplots(figsize=(10,10))
        ax.set_title("TSNE")
        
        cmap = plt.get_cmap("brg")
        for i, label in enumerate(countries):
            cval = cmap(predicts[i] / 4)
            ax.scatter(t_sne[i, 0], t_sne[i, 1], color=cval)
            ax.annotate(label, xy=(t_sne[i, 0], t_sne[i, 1]),fontsize=5, color=cval)

        fig.savefig('99.png',dpi=320, format='png', bbox_inches='tight') 
        
if __name__ == "__main__":
    _99()