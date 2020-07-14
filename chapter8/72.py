from nltk import stem
from nltk.corpus import stopwords
STOP_WORDS = stopwords.words('english')


def checkstopwords(word):
    """
    >>> checkstopwords("i")
    True
    >>> checkstopwords("me")
    True
    >>> checkstopwords("won")
    True
    >>> checkstopwords("point")
    False
    >>> checkstopwords("cabocha")
    False
    """
    return word.lower() in STOP_WORDS

def _72():
    stemmer = stem.PorterStemmer()
    features = []

    with open("sentiment.txt", "r", encoding="latin_1") as target:
        for line in target:
            line = line.rstrip()
            line_features = []
            for word in line.split():
                if word in ["," , "." , ":" , ";", "--", "-"]: continue
                if not checkstopwords(word):
                    feature = stemmer.stem(word)
                    line_features.append(feature)
            features.append(" ".join(line_features))

    print("\n".join(features))


if __name__ == "__main__":
    _72()

"""
結果
-1 instead let laugh come may lawrenc unleash trademark misogyni er comedi like human volcano overflow septic tank take pick
-1 rare movi intellig one everi regard except storylin everyth that' good ultim scuttl plot that' bore obviou
+1 [allen] manag breath life somewhat tire premis
+1 larg cast repres broad cross-sect tavernier' film bound along rat-a-tat energi " girl friday " maintain light touch tackl seriou theme
+1 establish omin mood tension swiftli suspens never rise higher level nevertheless maintain throughout
-1 suffer flat script low budget
"""

"""
元
-1 instead of letting the laughs come as they may , lawrence unleashes his trademark misogyny -- er , comedy -- like a human volcano or an overflowing septic tank , take your pick .
-1 it's rare that a movie can be as intelligent as this one is in every regard except its storyline ; everything that's good is ultimately scuttled by a plot that's just too boring and obvious .
+1 [allen] manages to breathe life into this somewhat tired premise .
+1 with a large cast representing a broad cross-section , tavernier's film bounds along with the rat-a-tat energy of " his girl friday , " maintaining a light touch while tackling serious themes .
+1 it establishes its ominous mood and tension swiftly , and if the suspense never rises to a higher level , it is nevertheless maintained throughout .
-1 suffers from a flat script and a low budget .
+1 'barbershop " is a good-hearted ensemble comedy with a variety of quirky characters and an engaging story .
"""