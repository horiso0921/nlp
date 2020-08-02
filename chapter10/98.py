from matplotlib import pyplot as plt
import numpy as np


def _98():
    from scipy.cluster.hierarchy import ward, dendrogram
    matries = np.empty([0, 300], dtype=np.float64)
    countries = []
    with open("96") as target:
        for line in target:
            word, matrix = line.strip().split("\t")
            matrix = np.array(list(map(np.float64, matrix.split())))
            matries = np.vstack([matries, matrix])
            countries.append(word)

        ward = ward(matries)
        print(ward)

        fig, ax = plt.subplots(1, 1, figsize=(100,50))
        ax.set_title('Hierarchical Clustering Dendrogram')
        ax.set_xlabel('distance')
        ax.set_ylabel('country')
        dendrogram(
            ward, 
            orientation='left',
            leaf_rotation=0., 
            labels=countries, 
            leaf_font_size=8) 
        ax.yaxis.set_label_position('right')
        fig.savefig('98.png',dpi=320, format='png', bbox_inches='tight') 
        
if __name__ == "__main__":
    _98()