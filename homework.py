import pickle

bogan = str(input('>> '))

print(pickle.load(open(bogan, "rb")))
