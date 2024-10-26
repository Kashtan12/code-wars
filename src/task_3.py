# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python

# solution by https://github.com/EmptyEXOT

def abbrev_name(name):
    return name.split()[0].capitalize()[0] + '.' + name.split()[1].capitalize()[0]
