import string
Sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
length = [sum(map(lambda literal: literal in string.ascii_letters, sub_string)) for sub_string in Sentence.split()]
print(length)
