# https://www.codewars.com/kata/53369039d7ab3ac506000467/train/python


def bool_to_word(boolean):
    if boolean is False:
        return ("No")
    if boolean is True:
        return ("Yes")


print(bool_to_word(False))
print(bool_to_word(True))