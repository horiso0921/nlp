from string import ascii_lowercase 
def cipher(target):
    return "".join(map(lambda literal:
        chr(219 - ord(literal)) if literal in ascii_lowercase else literal, target))
    
print(cipher("My name is Sota Horiuch1"))