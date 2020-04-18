from collections import defaultdict
words = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split()
dic = defaultdict(int)
for i, word in enumerate(words,start=1):
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        dic[word[0]] = i
    else:
        dic[word[:2]] = i
print(dict(dic))
