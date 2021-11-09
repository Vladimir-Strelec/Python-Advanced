def concatenate(*args):
    return "".join(list(map(str, args)))


print(concatenate("I", " ", "Love",  " ", "Python"))