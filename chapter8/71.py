"""
nltkというモジュールが優秀（以降も使う）
nltkにストップワードのリストがある（ずるかもしれない）
事前にpythonのインタラクティブシェルで次のコマンドを実行してstopwordをダウンロードしています
import nltk
nltk.download('stopwords')
"""
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

def _71():
    import doctest
    doctest.testmod()
    return


if __name__ == "__main__":
    _71()

"""
python 71.py -v
Trying:
    checkstopwords("i")
Expecting:
    True
ok
Trying:
    checkstopwords("me")
Expecting:
    True
ok
Trying:
    checkstopwords("won")
Expecting:
    True
ok
Trying:
    checkstopwords("point")
Expecting:
    False
ok
Trying:
    checkstopwords("cabocha")
Expecting:
    False
ok
2 items had no tests:
    __main__
    __main__._71
1 items passed all tests:
   5 tests in __main__.checkstopwords
5 tests in 3 items.
5 passed and 0 failed.
Test passed.
"""