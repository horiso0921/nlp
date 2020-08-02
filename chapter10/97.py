from sklearn.cluster import KMeans
import numpy as np
from collections import defaultdict

def _97():
    matries = np.empty([0, 300], dtype=np.float64)
    countries = []
    d = defaultdict(list)
    with open("96") as target:
        for line in target:
            word, matrix = line.strip().split("\t")
            matrix = np.array(list(map(np.float64, matrix.split())))
            matries = np.vstack([matries, matrix])
            countries.append(word)

        predicts = KMeans(n_clusters=5).fit_predict(matries)

        for predicts, country in sorted(zip(predicts, countries)):
            d[predicts].append(country)
    
    for i in range(5):
        with open("97_"+str(i), "w") as target:
            print("\n".join(d[i]), file=target)

if __name__ == "__main__":
    _97()

"""
0の一部
Australia 
Bangladesh 
China 
Fiji 
Guinea 
India 
Indonesia 
Japan 
1の一部
Andorra 
Antigua_and_Barbuda 
Arab_Republic_of_Egypt 
Argentine_Republic 
Bahamas 
Barbados 
Belize 
Benin 
Bolivarian_Republic_of_Venezuela 
Brunei_Darussalam 
Burundi 
2の一部
Argentina 
Belgium 
Brazil 
Canada 
Chile 
Colombia 
Cuba 
Dominican_Republic 
Ecuador 
France 
3の一部
Afghanistan 
Algeria 
Angola 
Bahrain 
Bhutan 
Botswana 
Burkina_Faso 
Cambodia 
Cameroon 
Congo 
4の一部
Albania 
Armenia 
Austria 
Azerbaijan 
Belarus 
Bosnia_and_Herzegovina 
Bulgaria 
Croatia 
Cyprus 
Czech_Republic 
Denmark 
Estonia 
"""